"""Static HTML/CSS for the app chrome. Palette: black · white · gold. All copy is original.
Colors that Streamlit draws itself (sidebar, buttons, links) are set in .streamlit/config.toml; this CSS refines the rest."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');
:root { --ink:#0B0B0B; --ink2:#1A1A1A; --gold:#C9A227; --gold-d:#A8841C; --gold-l:#E6C766; --gold-soft:#FBF6E8;
        --white:#FFFFFF; --mute:#5F5F5F; --line:#E8E4DA; }
html, body, .stMarkdown, p, li, button, input, textarea, label { font-family: 'Inter', sans-serif; }
h1, h2, h3, h4, .ns-serif { font-family: 'Playfair Display', Georgia, serif !important; color: var(--ink); letter-spacing: -0.01em; }
#MainMenu, footer, [data-testid="stDecoration"] { display: none !important; }
header[data-testid="stHeader"] { background: var(--white); border-bottom: 2px solid var(--gold); }
.block-container { max-width: 980px; padding-top: 4.2rem; padding-bottom: 8rem; }

/* ---------- buttons: black, gold on hover; primary = gold with black text (readable contrast) */
.stButton button, .stDownloadButton button, .stFormSubmitButton button {
  border-radius: 10px; min-height: 42px; font-weight: 500; border: 1px solid var(--line); background: var(--white); color: var(--ink); }
.stButton button:hover, .stDownloadButton button:hover { border-color: var(--gold); color: var(--gold-d); }
.stButton button[kind="primary"], .stFormSubmitButton button[kind="primary"] {
  background: var(--gold); border: 1px solid var(--gold); color: var(--ink) !important; font-weight: 600; }
.stButton button[kind="primary"]:hover { background: var(--ink); border-color: var(--ink); color: var(--gold-l) !important; }

/* ---------- home: simple welcome */
.ns-welcome { text-align: center; margin: 6vh auto 26px; max-width: 640px; }
.ns-mark { width: 64px; height: 64px; border-radius: 18px; background: var(--ink); color: var(--gold); display: inline-flex;
  align-items: center; justify-content: center; font-size: 30px; box-shadow: 0 10px 30px rgba(201,162,39,.25); }
.ns-welcome h1 { font-size: 2.35rem; margin: 18px 0 8px; }
.ns-welcome h1 em { font-style: normal; color: var(--gold-d); }
.ns-welcome p { color: var(--mute); font-size: 1.02rem; margin: 0; }
[class*="st-key-sugg"] button { justify-content: flex-start; text-align: left; min-height: 56px; border-radius: 14px;
  background: var(--white); border: 1px solid var(--line); box-shadow: 0 1px 2px rgba(0,0,0,.03); }
[class*="st-key-sugg"] button:hover { background: var(--gold-soft); border-color: var(--gold); color: var(--ink); }
.ns-wfoot { text-align: center; color: var(--mute); font-size: .82rem; margin-top: 18px; }
.ns-wfoot b { color: var(--ink); }

/* ---------- chat */
[data-testid="stChatMessage"] { background: var(--white); border: 1px solid var(--line); border-radius: 16px; padding: 14px 18px; }
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) { flex-direction: row-reverse; background: var(--ink);
  border-color: var(--ink); margin-left: 14%; }
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) * { color: #F4F4F4 !important; }
[data-testid="stChatMessageAvatarUser"] { background: var(--gold) !important; }
[data-testid="stChatMessage"] h4 { font-size: 1.05rem; margin-top: .9rem; border-left: 3px solid var(--gold); padding-left: 8px; }
[data-testid="stChatMessage"] a { color: var(--gold-d); }
[data-testid="stChatInput"] { border-radius: 16px; border: 1.5px solid var(--ink) !important; }
[data-testid="stChatInput"]:focus-within { border-color: var(--gold) !important; box-shadow: 0 0 0 3px rgba(201,162,39,.18); }
[data-testid="stBottomBlockContainer"] { background: linear-gradient(180deg, rgba(255,255,255,0) 0%, #fff 35%); }
.stTabs [aria-selected="true"] { color: var(--ink) !important; }
.stTabs [data-baseweb="tab-highlight"] { background: var(--gold) !important; }

/* ---------- sidebar (colors from config.toml [theme.sidebar]) */
[data-testid="stSidebar"] .stButton button { width: 100%; justify-content: flex-start; text-align: left; border: none;
  background: transparent; color: #EDEDED; font-size: .88rem; min-height: 36px; }
[data-testid="stSidebar"] .stButton button:hover { background: #1E1E1E; color: var(--gold-l); }
[data-testid="stSidebar"] .stButton button[kind="primary"] { background: var(--gold); color: var(--ink) !important; justify-content: center; }
.ns-side-label { font-size: .72rem; letter-spacing: .12em; text-transform: uppercase; color: var(--gold) !important; font-weight: 700; margin: 16px 0 4px; }
.ns-small { font-size: .75rem; color: #9A9A9A !important; line-height: 1.5; }

/* ---------- 'How it works' page */
.ns-eyebrow { color: var(--gold-d); font-weight: 700; font-size: .76rem; letter-spacing: .14em; text-transform: uppercase; }
.ns-hero { display: grid; grid-template-columns: 1.15fr 1fr; gap: 36px; align-items: center; margin: 8px 0 18px; }
.ns-hero h1 { font-size: 2.6rem; line-height: 1.12; margin: 12px 0; }
.ns-hero h1 em { font-style: normal; color: var(--gold-d); }
.ns-muted, .ns-hero p { color: var(--mute); font-size: 1.02rem; line-height: 1.6; }
.ns-chip { display: inline-block; border: 1px solid var(--line); background: var(--white); border-radius: 999px; padding: 6px 13px; margin: 0 6px 8px 0; font-size: .84rem; }
.ns-window { background: var(--white); border: 1px solid var(--line); border-radius: 18px; box-shadow: 0 18px 40px rgba(0,0,0,.08); overflow: hidden; }
.ns-wbar { background: var(--ink); color: var(--gold-l); padding: 10px 14px; font-size: .85rem; font-weight: 600; }
.ns-wbar i { display: inline-block; width: 9px; height: 9px; border-radius: 50%; background: #ffffff44; margin-right: 5px; }
.ns-wbody { padding: 14px; display: flex; flex-direction: column; gap: 10px; }
.ns-b { max-width: 88%; padding: 9px 12px; border-radius: 14px; font-size: .86rem; line-height: 1.45; }
.ns-b.bot { background: #F5F3EE; color: var(--ink); border-top-left-radius: 4px; }
.ns-b.me { background: var(--ink); color: #fff; align-self: flex-end; border-top-right-radius: 4px; }
.ns-b .ok { color: var(--gold-d); font-weight: 600; }
.ns-sec { margin-top: 46px; }
.ns-sec h2 { font-size: 1.8rem; margin: 6px 0 16px; }
.ns-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.ns-card { background: var(--white); border: 1px solid var(--line); border-radius: 16px; padding: 20px; transition: all .15s ease; }
.ns-card:hover { border-color: var(--gold); box-shadow: 0 10px 24px rgba(0,0,0,.06); transform: translateY(-2px); }
.ns-ico { width: 40px; height: 40px; border-radius: 10px; background: var(--ink); color: var(--gold); display: flex; align-items: center; justify-content: center; font-size: 1.15rem; margin-bottom: 10px; }
.ns-card h4 { margin: 0 0 6px; font-size: 1.05rem; } .ns-card p { margin: 0; color: var(--mute); font-size: .9rem; line-height: 1.5; }
.ns-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.ns-step .n { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 2.4rem; color: var(--gold); }
.ns-step h4 { margin: 2px 0 6px; } .ns-step p { color: var(--mute); font-size: .92rem; margin: 0; }
.ns-laws { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; }
.ns-law { border: 1px solid var(--line); border-left: 3px solid var(--gold); border-radius: 10px; padding: 10px 12px; background: var(--white); }
.ns-law b { display: block; font-size: .92rem; } .ns-law span { color: var(--mute); font-size: .78rem; }
.ns-lawlist { margin: 6px 0 0 16px; padding: 0; font-size: .78rem; color: var(--ink); } .ns-lawlist li { margin: 2px 0; }
.ns-cta { background: var(--ink); border-radius: 20px; padding: 32px; text-align: center; margin-top: 46px; }
.ns-prob { border: 1px solid var(--line); border-top: 3px solid var(--gold); border-radius: 14px; padding: 16px; background: var(--white); min-height: 150px; }
.ns-prob .i { font-size: 1.6rem; } .ns-prob h4 { margin: 6px 0 4px; font-size: 1.02rem; } .ns-prob p { color: var(--mute); font-size: .86rem; margin: 0; }
.ns-cta h2 { color: var(--gold-l) !important; margin: 0 0 6px; } .ns-cta p { color: #CFCFCF; margin: 0; }
.ns-foot { background: var(--ink); color: #BDBDBD; border-radius: 20px; padding: 24px 28px; margin-top: 16px; font-size: .86rem; border-top: 2px solid var(--gold); }
.ns-foot a { color: #fff; text-decoration: none; margin-right: 16px; } .ns-foot a:hover { color: var(--gold-l); } .ns-foot b { color: var(--gold-l); }
@media (max-width: 800px) { .ns-hero, .ns-grid, .ns-steps { grid-template-columns: 1fr; } .ns-hero h1, .ns-welcome h1 { font-size: 1.9rem; }
  [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) { margin-left: 4%; } }
</style>
"""

BRAND = "Suit Up"                      # change the product name here (also assets/logo.svg)
TAGLINE = "Suit up. Stand up for what's yours."

WELCOME = f"""<div class="ns-welcome"><div class="ns-mark">⚖</div>
<h1>Tell me what happened.</h1>
<p>Deposit not returned · refund not received · salary withheld · a notice you received.<br>
Type, tap 🎤 to speak, or 📎 attach a PDF — in English, हिन्दी or Hinglish. I'll ask a few questions first, like a lawyer would.</p></div>"""

SUGGESTIONS = [
    ("🏠 Landlord not returning my deposit", "Mera makaan maalik 45,000 deposit wapas nahi de raha. Maine 31 August 2026 ko Pune mein flat chhoda tha. Agreement aur UPI receipt hai."),
    ("🛒 Refund approved but never received", "I ordered a phone for Rs 18,999 on 2 Sept 2026 and got an empty box. The refund was approved but not received for 2 months. I live in Jaipur."),
    ("💼 Company holding my final salary", "I resigned and my last day was 31 August 2026. My company in Gurgaon is holding my final settlement of Rs 85,000 for 90 days."),
    ("📨 I got a notice from my landlord", "मुझे मकान मालिक का नोटिस आया है कि मैंने दीवार खराब की इसलिए 20,000 रुपये दो, वरना डिपॉज़िट नहीं मिलेगा। मैं लखनऊ में रहता हूँ। क्या करूँ?"),
]

WELCOME_FOOT = """<div class="ns-wfoot">Legal information, not legal advice · Free legal aid: <b>NALSA 15100</b> · Emergency <b>112</b></div>"""

HERO = f"""<div class="ns-hero"><div><span class="ns-eyebrow">⚖ {BRAND} — free legal help for everyday India</span>
<h1>Your money is stuck?<br><em>{TAGLINE}</em></h1>
<p>A deposit the landlord won't return. A refund that never came. Salary that stopped. A notice you don't understand.
Most people give up because a lawyer feels expensive and the process confusing. {BRAND} talks to you in Hindi, English or Hinglish,
asks the right questions, tells you where you stand under Indian law — with sources — and writes the letter you need.</p>
<span class="ns-chip">🗣️ Hindi · English · Hinglish</span><span class="ns-chip">🎤 Speak or type</span><span class="ns-chip">📎 Reads your PDFs</span>
<span class="ns-chip">✅ Checked citations</span><span class="ns-chip">💸 Free</span></div>
<div class="ns-window"><div class="ns-wbar"><i></i><i></i><i></i>&nbsp; {BRAND}</div><div class="ns-wbody">
<div class="ns-b me">Makaan maalik 30,000 deposit wapas nahi de raha. Varanasi, 30 Sept ko kamra chhoda.</div>
<div class="ns-b bot">Samajh gaya. Advice se pehle 2 sawaal: 1) Kya likhit rent agreement hai? 2) Maalik kis cheez ki katauti bol raha hai?</div>
<div class="ns-b me">Agreement hai. Painting ka bol raha hai.</div>
<div class="ns-b bot">UP mein deposit vacant possession milne par wapas karna hota hai <span class="ok">✅ UP Tenancy Act, 2021 — s. 11</span>.
Pehla step: likhit demand. Notice draft kar doon? 📄</div></div></div></div>"""

PROBLEMS = [
    ("🏠", "Security deposit", "Landlord keeping your deposit, or cutting money for 'painting' and 'damages'.", 0),
    ("🛒", "Refund or defective product", "Refund approved but never paid, order not delivered, product broken and service not fixing it.", 1),
    ("💼", "Unpaid salary / F&F", "Salary delayed, full-and-final settlement or gratuity held back after you left.", 2),
    ("📨", "A notice you received", "Your landlord, employer or a company sent you a notice demanding money — what does it mean, how to reply.", 3),
]

HOW = """<div class="ns-sec" id="how"><div class="ns-eyebrow">How it works</div><h2>From your story to your next move</h2>
<div class="ns-steps">
<div class="ns-step"><div class="n">01</div><h4>Tell your story</h4><p>Type, speak or attach your agreement / notice / bill — in the language you're comfortable with.</p></div>
<div class="ns-step"><div class="n">02</div><h4>Answer a few questions</h4><p>Like a lawyer, it first asks what matters: dates, place, amount, proof, what you've tried. You can skip.</p></div>
<div class="ns-step"><div class="n">03</div><h4>Get your plan & documents</h4><p>Case summary, the law that applies, options from cheapest to formal, deadlines — and a draft to send.</p></div>
</div></div>"""

FEATURES = """<div class="ns-sec" id="features"><div class="ns-eyebrow">What you get</div><h2>Everything you need to act — not just an answer</h2>
<div class="ns-grid">
<div class="ns-card"><div class="ns-ico">🗂️</div><h4>Your case, organised</h4><p>A messy story becomes a timeline, the proof you have, and the proof you still need.</p></div>
<div class="ns-card"><div class="ns-ico">⚖️</div><h4>Where you stand</h4><p>The law in plain words, your strengths and weak points, and options ranked from a WhatsApp message to a formal complaint.</p></div>
<div class="ns-card"><div class="ns-ico">📄</div><h4>Ready-to-send drafts</h4><p>WhatsApp demand, legal notice, reply to a notice, consumer complaint, wage-claim application — as Word files.</p></div>
<div class="ns-card"><div class="ns-ico">📎</div><h4>Reads your documents</h4><p>Upload the rent agreement, offer letter or notice. It finds the clause that matters and quotes the page.</p></div>
<div class="ns-card"><div class="ns-ico">🎭</div><h4>Practise the conversation</h4><p>Rehearse with an AI playing your landlord, the company or HR — then get coaching on what to say.</p></div>
<div class="ns-card"><div class="ns-ico">🔊</div><h4>Listen, not just read</h4><p>Every answer can be read aloud — in Hindi or English — for anyone more comfortable listening.</p></div>
</div></div>"""

TRUST = """<div class="ns-sec" id="trust"><div class="ns-eyebrow">Why you can trust it</div><h2>Honest about what it knows — and what it doesn't</h2>
<div class="ns-grid">
<div class="ns-card"><div class="ns-ico">✅</div><h4>Checked law only</h4><p>Sections come from a small knowledge base, each checked against the Act's text and linked to its source. The AI cites them by ID — it never types a section number itself.</p></div>
<div class="ns-card"><div class="ns-ico">⚠️</div><h4>Uncertainty is labelled</h4><p>Anything outside the checked list is marked “verify”. Outdated laws are caught (🔄 Payment of Wages Act → Code on Wages, 2019). Court cases are never quoted.</p></div>
<div class="ns-card"><div class="ns-ico">🧑‍⚖️</div><h4>Knows when you need a lawyer</h4><p>Police cases, court papers, large amounts or threats → it says so plainly and gives free legal-aid contacts (NALSA 15100).</p></div>
</div></div>"""

NOT_COVERED = """<div class="ns-sec" id="limits"><div class="ns-eyebrow">What it does not handle</div><h2>Outside these four problems, it won't guess</h2>
<p class="ns-muted">FIR or police case against you · court summons · cheque bounce · divorce, custody, domestic violence · land and inheritance ·
builder/flat disputes · cyber fraud. For these you get the right help instead: <b>NALSA legal aid 15100</b> · <b>Emergency 112</b> ·
<b>Women 181</b> · <b>Cyber crime 1930</b> · <b>Tele-MANAS 14416</b>.</p></div>"""

FAQ = [
    ("Is this a lawyer?", f"No. {BRAND} gives legal information and drafts to help you act on your own. For police cases, court papers, large amounts or anything urgent it tells you to contact a lawyer — free legal aid is available on NALSA 15100."),
    ("Can I trust the sections it cites?", "Citations marked ✅ come from a checked list with sources. Anything marked ⚠️ was recalled by the AI and must be checked on indiacode.nic.in. Court judgments are never quoted, because AI often invents them."),
    ("Why does it ask questions first?", "The answer depends on details — your state (tenancy law differs), dates (time limits), amounts (which forum), and proof. Asking first avoids confident advice built on wrong assumptions. You can always press “Skip”."),
    ("What happens to my documents and chats?", "They are saved with your private link so you can come back. “Delete this consultation” removes the chat and its documents. Don't upload Aadhaar/PAN or passwords."),
    ("Why doesn't the microphone work?", "Browsers allow the microphone only on https:// pages or on localhost. Use the app's https link (or http://localhost:8501 on your own computer) and allow microphone access."),
    ("Which languages work?", "English, Hindi and Hinglish — typing or speaking, and answers can be read aloud. Drafted legal documents are in English, as Indian offices and courts usually expect."),
    ("Does it cost anything?", "No. It runs on free tiers; it may slow down when many people use it at once."),
]

CTA_FOOT = f"""<div class="ns-cta"><h2>Don't give up on what's yours.</h2><p>Most everyday disputes end with one clear, firm letter. Start by telling {BRAND} what happened.</p></div>
<div class="ns-foot"><b>⚖ {BRAND}</b> — legal information for India, not legal advice.<br><br>
<b>Official help:</b> <a href="https://nalsa.gov.in" target="_blank">NALSA legal aid 15100</a><a href="https://e-jagriti.gov.in" target="_blank">e-Jagriti (consumer complaints)</a>
<a href="https://consumerhelpline.gov.in" target="_blank">Consumer helpline 1915</a><a href="https://www.indiacode.nic.in" target="_blank">India Code</a><br><br>
Emergency 112 · Women helpline 181 · Cyber crime 1930 · Tele-MANAS 14416</div>"""
