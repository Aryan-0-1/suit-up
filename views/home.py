"""Landing page (default): what the app does, for which problems, how it stays honest, what it won't handle."""
import streamlit as st

from core import kb, ui

CHAT = "views/chat.py"


def start(prompt: str | None = None):
    if prompt:
        st.session_state.pending_prompt = prompt   # the chat page sends it on arrival
        st.session_state.pop("thread", None)       # fresh consultation for an example
    st.switch_page(CHAT)


st.markdown(ui.HERO, unsafe_allow_html=True)
c1, c2, _ = st.columns([1.2, 1.2, 3])
if c1.button("Start my case  →", type="primary", use_container_width=True):
    start()
if c2.button("See an example", use_container_width=True):
    start(ui.SUGGESTIONS[0][1])

st.markdown('<div class="ns-sec" id="problems"><div class="ns-eyebrow">Four problems, handled well</div>'
            '<h2>Which one is yours?</h2></div>', unsafe_allow_html=True)
cols = st.columns(4)
for col, (icon, title, desc, ex) in zip(cols, ui.PROBLEMS):
    with col:
        st.markdown(f'<div class="ns-prob"><div class="i">{icon}</div><h4>{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)
        if st.button("Try an example", key=f"p{ex}", use_container_width=True, help=ui.SUGGESTIONS[ex][1]):
            start(ui.SUGGESTIONS[ex][1])

st.markdown(ui.HOW + ui.FEATURES + ui.TRUST, unsafe_allow_html=True)

# Laws covered — generated from the knowledge base, so this list is always accurate
LABELS = {"deposit": "🏠 Security deposit", "consumer": "🛒 Refunds & defective products", "salary": "💼 Unpaid salary & F&F",
          "notice": "📨 A notice you received", "referral": "⚖️ Free legal aid"}
groups = {}
for e in kb.load().values():
    groups.setdefault(e["category"], []).append(e)


def _label(e):
    sec = str(e["section"])
    name = e["title"] if e["act"].startswith("General") else e["act"]
    return name + ("" if sec in ("none", "process", "status", "model", "rules") else f" — {'s. ' if sec[0].isdigit() else ''}{sec}")


cards = "".join(f'<div class="ns-law"><b>{label}</b><span>{len(groups.get(a, []))} checked entries</span><ul class="ns-lawlist">'
                + "".join(f"<li>{_label(e)}</li>" for e in groups.get(a, [])) + "</ul></div>" for a, label in LABELS.items())
st.markdown(f'<div class="ns-sec" id="laws"><div class="ns-eyebrow">Laws covered</div><h2>A small, checked knowledge base</h2>'
            f'<p class="ns-muted">Every entry was checked against the text of the law on 8 Nov 2026 and carries a source link and a confidence level.</p>'
            f'<div class="ns-laws">{cards}</div></div>', unsafe_allow_html=True)
st.markdown(ui.NOT_COVERED, unsafe_allow_html=True)

st.markdown('<div class="ns-sec" id="faq"><div class="ns-eyebrow">FAQ</div><h2>Questions people ask</h2></div>', unsafe_allow_html=True)
for q, a in ui.FAQ:
    with st.expander(q):
        st.write(a)
st.markdown(ui.CTA_FOOT, unsafe_allow_html=True)
if st.button("Start my case  →", type="primary", key="start_bottom"):
    start()
