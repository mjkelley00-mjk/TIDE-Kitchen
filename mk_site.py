# Generates request.html, partner-room.html and company-room.html for tide.kitchen (TIDE data room).
import html, re
SITE='/tmp/claude-0/work/site/'
EXEC_URL='https://script.google.com/macros/s/AKfycbziJ1wsEfBW3cs_wdorrGMOQ7e46B0FjyDRJuHq89nN9ErAem1HDnTFJw9lII9NSk2t2Q/exec'   # set after the Apps Script web app is deployed
HEAD='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="robots" content="noindex, nofollow">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{--ink-deep:#061726; --ink:#0a1f33; --ink-soft:#1a3a57; --paper:#f5f1e8; --gold:#c9a961;
    --text-paper:#efe9d9; --text-paper-mute:rgba(239,233,217,0.66);
    --font-display:'EB Garamond','Times New Roman',Georgia,serif; --font-body:'Inter',-apple-system,sans-serif; --font-mono:'JetBrains Mono',ui-monospace,monospace;}
  *{box-sizing:border-box; margin:0; padding:0;}
  [hidden]{display:none !important;}
  body{background:var(--ink-deep); color:var(--text-paper); font-family:var(--font-body); font-size:16px; line-height:1.55; min-height:100vh; display:flex; flex-direction:column;}
  a{color:inherit;}
  .topbar{display:flex; justify-content:space-between; align-items:center; gap:16px; padding:26px clamp(20px,5vw,56px); border-bottom:1px solid var(--ink-soft);}
  .topbar__brand{font-family:var(--font-mono); font-size:14px; letter-spacing:.24em; text-transform:uppercase; color:var(--paper); text-decoration:none; font-weight:500;}
  .topbar__brand em{color:var(--gold); font-style:normal;}
  .topbar__back{font-family:var(--font-mono); font-size:12px; letter-spacing:.08em; color:var(--text-paper-mute); text-decoration:none;}
  .topbar__back:hover{color:var(--gold);}
  main{flex:1; width:100%%; max-width:820px; margin:0 auto; padding:clamp(40px,8vh,88px) clamp(20px,5vw,56px) 64px;}
  .eyebrow{font-family:var(--font-mono); font-size:12px; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); margin-bottom:16px;}
  h1{font-family:var(--font-display); font-weight:500; font-size:clamp(34px,6vw,56px); line-height:1.04; margin-bottom:18px; text-wrap:balance;}
  h1 em{color:var(--gold); font-style:italic;}
  h2{font-family:var(--font-display); font-weight:500; font-size:26px; line-height:1.15; margin-bottom:14px;}
  .lead{color:var(--text-paper-mute); font-size:clamp(16px,2vw,18px); line-height:1.6; max-width:640px; margin-bottom:36px;}
  footer{border-top:1px solid var(--ink-soft); padding:28px clamp(20px,5vw,56px); display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px; font-size:12px; color:var(--text-paper-mute);}
  footer a{color:var(--text-paper-mute); text-decoration:none;}
  footer a:hover{color:var(--gold);}
  a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:2px solid var(--gold); outline-offset:2px;}
%s
</style>
</head>
<body>
  <div class="topbar">
    <a class="topbar__brand" href="/">TIDE <em>·</em> KITCHEN</a>
    <a class="topbar__back" href="/">← Back to site</a>
  </div>
'''
FOOT='''  <footer>
    <div>© 2026 TIDE Kitchen · Not an offer of securities</div>
    <div><a href="mailto:hello@tide.kitchen">hello@tide.kitchen</a> &nbsp;·&nbsp; <a href="/">tide.kitchen</a></div>
  </footer>
%s</body>
</html>
'''
# ---------------- request page ----------------
REQ_CSS='''  .steps{display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-bottom:40px; max-width:720px;}
  .steps > div{border-top:1px solid var(--gold); padding-top:14px;}
  .steps .n{font-family:var(--font-display); font-style:italic; font-size:26px; color:var(--gold); line-height:1;}
  .steps .t{font-weight:600; font-size:15px; margin-top:8px;}
  .steps .d{color:var(--text-paper-mute); font-size:14px; margin-top:4px;}
  form{display:grid; grid-template-columns:minmax(0,1fr); gap:20px; max-width:680px;}
  .rowf{display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:20px;}
  .field{display:flex; flex-direction:column; gap:8px;}
  .field label{font-family:var(--font-mono); font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--text-paper-mute);}
  .field label span{text-transform:none; letter-spacing:0;}
  .field input,.field select,.field textarea{background:rgba(239,233,217,0.05); border:1px solid #4a6a88; border-radius:6px; padding:13px 15px; color:var(--text-paper); font-family:var(--font-body); font-size:15px;}
  .field input::placeholder,.field textarea::placeholder{color:rgba(239,233,217,0.58);}
  .field input:focus,.field select:focus,.field textarea:focus{border-color:var(--gold);}
  .field select{appearance:none; -webkit-appearance:none; cursor:pointer; background-color:var(--ink);}
  .field select option{background-color:var(--ink); color:var(--text-paper);}
  .field textarea{min-height:104px; resize:vertical;}
  .hint{font-size:12px; color:var(--text-paper-mute);}
  .ack{display:flex; gap:10px; align-items:flex-start; font-size:13px; color:var(--text-paper-mute); line-height:1.5;}
  .ack input{margin-top:2px; width:16px; height:16px; flex:none; accent-color:var(--gold);}
  .submit{justify-self:start; margin-top:6px; background:var(--gold); color:var(--ink); border:none; border-radius:30px; padding:15px 36px; font-family:var(--font-body); font-weight:600; font-size:15px; cursor:pointer;}
  .submit:hover{opacity:.9;}
  .fine{font-size:12px; color:var(--text-paper-mute); margin-top:2px; line-height:1.55;}
  .formstatus{margin-top:24px; padding:18px 20px; border:1px solid var(--gold); border-radius:10px; background:rgba(201,169,97,0.12); color:var(--text-paper); font-size:16px; line-height:1.55; max-width:680px;}
  @media (max-width:640px){ .rowf{grid-template-columns:minmax(0,1fr);} .steps{grid-template-columns:1fr;} }'''
REQ_BODY='''  <main>
    <div class="eyebrow">For funders, partners and advisors</div>
    <h1>Request <em>detailed materials.</em></h1>
    <p class="lead">The website gives the outline. Detailed materials are shared by invitation.</p>
    <div class="steps">
      <div><div class="n">1</div><div class="t">Tell us who you are</div><div class="d">A few details so we know what will be useful to you.</div></div>
      <div><div class="n">2</div><div class="t">We follow up by email</div><div class="d">We read every request and reply personally.</div></div>
      <div><div class="n">3</div><div class="t">You get an invitation</div><div class="d">A private page and a shared folder with the documents.</div></div>
    </div>
    <form action="__EXEC__" method="POST">
      <input type="hidden" name="form_type" value="Materials request">
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;opacity:0;height:0;width:0;">
      <div class="rowf">
        <div class="field"><label for="rq-name">Full name</label><input id="rq-name" name="name" type="text" required maxlength="120" placeholder="Your name" autocomplete="name"></div>
        <div class="field"><label for="rq-email">Email</label><input id="rq-email" name="email" type="email" required maxlength="160" placeholder="you@organization.com" autocomplete="email"></div>
      </div>
      <div class="rowf">
        <div class="field"><label for="rq-org">Organization</label><input id="rq-org" name="organization" type="text" required maxlength="160" placeholder="Your organization" autocomplete="organization"></div>
        <div class="field"><label for="rq-type">I&rsquo;m with a&hellip;</label>
          <select id="rq-type" name="inquirer_type" required>
            <option value="">Select&hellip;</option><option>Foundation or impact funder</option><option>Family office</option><option>Fund or institution</option><option>Individual</option><option>Development or real estate firm</option><option>Bank or lender</option><option>Public or civic organization</option><option>Restaurant or franchise company</option><option>Advisor</option><option>Other</option>
          </select>
        </div>
      </div>
      <div class="rowf">
        <div class="field"><label for="rq-int">I&rsquo;m interested in</label>
          <select id="rq-int" name="interest" required><option value="">Select&hellip;</option><option>Funding the platform</option><option>A partner site or development partnership</option><option>Lending to operators</option><option>Public or philanthropic partnership</option><option>Advising</option><option>Learning more about TIDE Kitchen</option></select>
        </div>
        <div class="field"><label for="rq-gmail">Google account email <span>(optional)</span></label><input id="rq-gmail" name="google_email" type="email" maxlength="160" placeholder="If different from above"><span class="hint">Materials are shared through Google Drive.</span></div>
      </div>
      <div class="field"><label for="rq-msg">A few words on your interest</label><textarea id="rq-msg" name="message" required maxlength="2000" placeholder="What you&rsquo;re looking for, or how you heard about TIDE Kitchen"></textarea></div>
      <label class="ack"><input type="checkbox" name="confidentiality_ack" value="agreed" required> I understand that any materials TIDE Kitchen shares are confidential, and I agree not to distribute or reproduce them.</label>
      <label class="ack"><input type="checkbox" name="updates_ok" value="yes"> Optional: keep me posted on TIDE Kitchen&rsquo;s progress by email.</label>
      <button class="submit" type="submit">Send request</button>
      <p class="fine">We&rsquo;ll review and follow up by email. Nothing on this site is an offer to sell, or a solicitation of an offer to buy, any security. Submitting creates no commitment and is not investment advice. Materials are shared at TIDE Kitchen&rsquo;s discretion. By submitting, you consent to TIDE Kitchen contacting you about your request.</p>
    </form>
  </main>
'''
REQ_JS='''<script>
  (function(){
    var form = document.querySelector('form');
    if(!form) return;
    var status = document.createElement('p');
    status.className='formstatus'; status.setAttribute('role','status'); status.setAttribute('aria-live','polite');
    status.hidden = true;
    form.parentNode.insertBefore(status, form.nextSibling);
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var orig = btn.textContent;
      btn.disabled = true; btn.textContent = 'Sending\\u2026';
      // The Google Apps Script endpoint returns no CORS headers, so the response is opaque;
      // a completed request is treated as received.
      fetch(form.action, { method:'POST', body:new FormData(form), mode:'no-cors' })
        .then(function(){
          form.reset(); form.hidden = true;
          status.textContent = 'Thank you. Your request has been received, and we\\u2019ll follow up by email.';
          status.hidden = false;
          status.scrollIntoView({behavior:'smooth', block:'center'});
        })
        .catch(function(){
          status.textContent = 'Something went wrong. Please email hello@tide.kitchen.';
          status.hidden = false;
          btn.disabled = false; btn.textContent = orig;
        });
    });
  })();
</script>
'''
open(SITE+'request.html','w').write(HEAD%('Request Materials — TIDE Kitchen',REQ_CSS)+REQ_BODY.replace('__EXEC__',EXEC_URL)+FOOT%REQ_JS)

# ---------------- room pages ----------------
ROOM_CSS='''  .notice{border-left:3px solid var(--gold); background:rgba(239,233,217,0.05); padding:14px 18px; font-size:14px; color:var(--text-paper-mute); border-radius:0 8px 8px 0; margin-bottom:32px;}
  .notice strong{color:var(--text-paper); font-weight:600;}
  .how{border:1px solid var(--ink-soft); border-radius:10px; padding:22px 24px; margin-bottom:40px; background:var(--ink);}
  .how ul{padding-left:20px; display:flex; flex-direction:column; gap:6px; font-size:15px; color:var(--text-paper-mute);}
  ol.docs{list-style:none; border-top:1px solid var(--gold);}
  ol.docs li{display:grid; grid-template-columns:40px minmax(0,1fr) auto; gap:6px 16px; align-items:start; padding:20px 0; border-bottom:1px solid var(--ink-soft);}
  .n{font-family:var(--font-display); font-style:italic; font-size:28px; color:var(--gold); line-height:1.05; font-variant-numeric:tabular-nums;}
  .t{font-weight:600; font-size:17px;}
  .d{color:var(--text-paper-mute); font-size:15px; margin-top:3px;}
  .meta{font-family:var(--font-mono); font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--text-paper-mute); margin-top:8px;}
  a.open{display:inline-block; background:var(--gold); color:var(--ink); font-weight:600; font-size:14px; text-decoration:none; padding:9px 18px; border-radius:30px; white-space:nowrap;}
  a.open:hover{opacity:.9;}
  a.plain{color:var(--gold);}
  .after{color:var(--text-paper-mute); font-size:15px; margin-top:16px;}
  .contact{color:var(--text-paper-mute); font-size:15px; margin-top:36px;}
  .contact b{color:var(--text-paper); font-weight:600; user-select:all;}
  @media (max-width:560px){ ol.docs li{grid-template-columns:30px minmax(0,1fr);} ol.docs li a.open{grid-column:2; justify-self:start;} }'''
G='https://drive.google.com/file/d/%s/view'
def room(fname,title,eyebrow,h1,lede,rules,docs,folder,model_line=True):
    li=''.join(f'<li><div class="n">{i}</div><div><div class="t">{html.escape(t)}</div><div class="d">{d}</div><div class="meta">{m}</div></div><a class="open" href="{G%u}" target="_blank" rel="noopener">Open</a></li>\n      ' for i,(t,d,m,u) in enumerate(docs,1))
    body=f'''  <main>
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="lead">{lede}</p>
    <div class="notice"><strong>Shared by invitation. October 2026.</strong> Not an offer to sell or a solicitation to buy any security. Figures are planning estimates from a model on stated assumptions, not a forecast. Legal, tax and securities treatments are open until counsel confirms them.</div>
    <section class="how"><h2>How to use this data room</h2>
      <ul>{rules}<li>Please don&rsquo;t forward files or this page. Ask us to add a colleague and we will invite them directly.</li><li>Files are updated in place, so a link always opens the current version.{' The model version (v7.5) is the number to quote if you send questions.' if model_line else ''}</li></ul>
    </section>
    <section><h2>Documents, in reading order</h2>
      <ol class="docs">
      {li}</ol>
      <p class="after">Each document opens in Google Drive and needs the Google account your invitation was sent to. <a class="plain" href="https://drive.google.com/drive/folders/{folder}" target="_blank" rel="noopener">Open the whole folder</a>.</p>
    </section>
    <p class="contact">Questions, or access for a colleague: Michael Kelley, Founder &amp; Managing Director · <b>hello@tide.kitchen</b></p>
  </main>
'''
    open(SITE+fname,'w').write(HEAD%(title,ROOM_CSS)+body+FOOT%'')
room('partner-room.html','TIDE Kitchen Partner Data Room','TIDE Kitchen · Partner Data Room','The platform, <em>in full.</em>',
 'For development partners, lenders, and public and philanthropic partners. How the incubator, the co-owned storefronts and the property vehicle work, with the evidence behind each assumption.',
 '<li>Start with the white paper. The plan and the comparables memo are for diligence.</li><li>These are partner editions of the full documents.</li>',
 [('White paper, partner edition','The whole design and the reasoning behind it: the market, the four stages, the co-owned storefront, partner sites, the property vehicle, community ownership, public return and risks.','PDF · 32 pages','1nzRsZoh2y11hKAnHUwtEuhKZR4m8reJV'),
  ('Business and operations plan, partner edition','How it runs: staffing, the incubator, store economics and buyouts, the site plan and what TIDE asks of a development partner, property, compliance and open items.','PDF · 16 pages','1KwJof6J_04jxRmykeOZpGYAgoXQAbBW5'),
  ('Comparables and validation, partner edition','The evidence file: each load-bearing assumption set against a named benchmark, from stall sales and store margins to rents, loan terms and the public-return method.','PDF · 20 pages','1xD-b38Mh_mt9eIfTqrX7PeB8McrlhkOW')],
 '1ILg3s3xCtbrUP4aIpdP8ID7hekiqbR1Z', model_line=False)
room('company-room.html','TIDE Kitchen Company Data Room','TIDE Kitchen · Company Data Room','The platform, the company <em>and the model.</em>',
 'The complete set: the summary and deck, the full analysis, the operating plan, the evidence file and the working model.',
 '<li>Start with the executive summary and the deck. The white paper, strategic analysis, plan, comparables and model are for diligence.</li><li>Document 8 is indicative and subject to counsel review.</li>',
 [('Executive summary','One page: the thesis, the model, the numbers and what is open.','PDF · 1 page','1VcsK9Ql_E46ofnQkAC3NkP1fmk_KagsY'),
  ('Pitch deck','The whole picture in 15 slides.','PDF · 15 slides','1FSMpCzDbTf9rDXdbjNivl0ZmHXx7W0pQ'),
  ('White paper','The full design and the reasoning behind it, including the capital architecture.','PDF · 39 pages','1rFGv-TX35bVNS3hML2Uep-Axzp0oICLP'),
  ('Strategic analysis','The detailed case, section by section, with the single-input risk tests and open items.','PDF · 28 pages','1NhASKAN4YHrT4XOpOx1K7y8U95dQxWYO'),
  ('Business and operations plan','How it runs: staffing, the incubator, stores and buyouts, the site plan, property, the funds and the company.','PDF · 17 pages','1HcsqQbKkuNIl5lYiyar9TySskYxMiHCd'),
  ('Comparables and validation','The evidence file: each load-bearing assumption set against a named benchmark.','PDF · 24 pages','15vmRKu6HUpH_fLfbQvHxDF1q8CKwUlPk'),
  ('Platform model v7.5','The complete workbook behind every figure. Blue cells on the Inputs tab are assumptions you can change in your own copy; the Risk Tests tab records each single-input test.','Excel workbook · 14 tabs','1zuznMnAX24We0ezsXHqYj_1wBGia2vmv'),
  ('Structure summary','Indicative terms. Non-binding and subject to counsel review.','PDF · 9 pages','1bFhLddWnchwGnrVwEMUyAtIJkQVcrnd4')],
 '1CYafrNY5nQM9laJzsPRmqfNAlEVSdAaY')
print('written')
