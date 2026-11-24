import streamlit as st
from app.storage import init_db, save_record, get_records, get_image_path
from app.analysis import make_preview, analyze_image
from app.comparison import compare_images

st.set_page_config(page_title="SkinSense", page_icon="🧴", layout="wide")
init_db()
st.title("🧴 SkinSense")
st.subheader("AI-powered skin health monitoring — early prototype")
st.warning("Educational prototype only. SkinSense does not diagnose skin conditions or recommend treatment. Image measurements vary with lighting and camera settings.")

record_tab, history_tab, compare_tab, about_tab = st.tabs(["New check-in", "History", "Compare photos", "About"])
with record_tab:
    photo = st.file_uploader("Upload a skin photo", type=["jpg", "jpeg", "png"])
    note = st.text_area("Optional notes")
    if photo:
        try:
            preview, image = make_preview(photo)
            st.image(preview, caption="Photo preview", width=420)
            metrics = analyze_image(image)
            c1, c2, c3 = st.columns(3)
            c1.metric("Width", f"{metrics['width']} px")
            c2.metric("Height", f"{metrics['height']} px")
            c3.metric("Average brightness", f"{metrics['brightness']:.1f}/255")
            st.caption("Technical image statistics only — not clinical measurements.")
            if st.button("Save check-in", type="primary"):
                save_record(photo.getvalue(), photo.name, note, metrics)
                st.success("Saved locally on this computer.")
        except Exception as e:
            st.error(f"Could not read image: {e}")

with history_tab:
    records = get_records()
    if not records:
        st.info("No saved check-ins yet.")
    for r in records:
        with st.expander(f"{r['created_at']} — {r['filename']}"):
            st.write(r["note"] or "No note")
            p = get_image_path(r["image_file"])
            if p.exists():
                st.image(str(p), width=360)
            st.caption(f"{r['width']} × {r['height']} px | Brightness {r['brightness']:.1f}/255")

with compare_tab:
    records = get_records()
    if len(records) < 2:
        st.info("Save at least two check-ins to compare photos.")
    else:
        options = {f"{r['created_at']} — {r['filename']}": r for r in records}
        names = list(options)
        first = st.selectbox("First photo", names, index=min(1, len(names)-1))
        second = st.selectbox("Second photo", names, index=0)
        if first != second:
            a, b = options[first], options[second]
            pa, pb = get_image_path(a["image_file"]), get_image_path(b["image_file"])
            col1, col2 = st.columns(2)
            col1.image(str(pa), caption="First photo", use_container_width=True)
            col2.image(str(pb), caption="Second photo", use_container_width=True)
            st.info(compare_images(pa, pb))
            st.caption("Differences may be caused by lighting, angle, distance, or camera settings.")

with about_tab:
    st.markdown("""
    **Implemented:** local photo check-ins, notes, history, basic image dimensions/brightness, and side-by-side comparison.

    **Not implemented:** trained AI, skin-condition classification, diagnosis, risk prediction, or treatment advice.

    **Future work:** define a safe intended use with qualified advisors; consider consented and licensed data; validate any future model; and add security/privacy controls before real-user deployment.
    """)
    st.caption("If a skin concern is persistent, painful, bleeding, rapidly changing, or worrying, consult a qualified healthcare professional.")
