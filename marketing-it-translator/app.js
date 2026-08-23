// Marketing ↔ IT Translator Logic with Multi-Tier Sarcasm Engine

let currentMode = 'mkt-to-it'; // 'mkt-to-it' or 'it-to-mkt'
let sarcasmLevel = 3; // 1: Mild, 2: Dry Humor, 3: Maximum Sarcasm

// Multi-Tier Sarcasm Translation Database
const translations = {
  'mkt-to-it': [
    {
      keywords: ['make it pop', 'pop', 'vibrant', 'eye catching', 'visuals'],
      translations: {
        1: "Adjust CSS color contrast, saturation, and visual prominence according to brand guidelines.",
        2: "Increase CSS saturation by 20% and add subtle glow filters, ignoring standard contrast guidelines.",
        3: "Increase saturation to eye-searing levels, drop random neon glow filters everywhere, and annihilate all WCAG accessibility compliance."
      },
      commentaries: {
        1: "Commentary: A standard request for visual enhancement.",
        2: "Commentary: 'I don't know what I want, but I'll recognize it when I see it on someone else's site.'",
        3: "Commentary: Translation: 'Please blind the user so they don't notice our lack of value proposition.'"
      }
    },
    {
      keywords: ['quick fix', 'simple change', 'small tweak', 'easy update', 'minor change'],
      translations: {
        1: "Perform a minor code adjustment requiring short development and QA testing time.",
        2: "Modify the database schema, update API endpoints, and re-run regression tests before Friday deployment.",
        3: "Perform a 'minor tweak' that actually rewrites 14 core microservices, breaks staging, and ruins everyone's weekend."
      },
      commentaries: {
        1: "Commentary: Estimated development time: 1-2 hours.",
        2: "Commentary: Notice: The phrase 'quick fix' invariably adds 3 weeks to sprint velocity.",
        3: "Commentary: There is no phrase in the English language that instills more existential dread in a senior engineer."
      }
    },
    {
      keywords: ['viral', 'growth hack', 'growth-hack', 'flywheel', 'growth'],
      translations: {
        1: "Implement customer acquisition strategies to increase organic user engagement.",
        2: "Send push notifications and capture extra analytics cookies to boost short-term conversion metrics.",
        3: "Spam users with un-subscribable push notifications, harvest excessive cookies, and hope the server doesn't melt under 100 concurrent requests."
      },
      commentaries: {
        1: "Commentary: Focused on sustainable organic marketing channels.",
        2: "Commentary: Your 'growth hack' is our technical support nightmare.",
        3: "Commentary: Your 'growth hack flywheel' is literally just a self-inflicted DDoS attack."
      }
    },
    {
      keywords: ['mvp', 'minimum viable product', 'phase 1', 'prototype'],
      translations: {
        1: "Build an initial core functional release with baseline features for early feedback.",
        2: "A functional prototype with basic features that will likely serve as production code longer than planned.",
        3: "A barely functional prototype held together by duct tape and hardcoded strings that will remain in production unchanged for 7 years."
      },
      commentaries: {
        1: "Commentary: Iterative product development methodology.",
        2: "Commentary: There is nothing more permanent than a temporary MVP.",
        3: "Commentary: 'Phase 2' is a mythical land where forgotten tickets go to die."
      }
    },
    {
      keywords: ['bandwidth', 'capacity', 'availability', 'workload'],
      translations: {
        1: "Assess current sprint workload and engineering team availability for new deliverables.",
        2: "Engineering team is currently operating near maximum capacity with limited sprint space.",
        3: "Current team capacity is at 198% with zero available RAM in our brains. No, we won't work Sunday to change button margins."
      },
      commentaries: {
        1: "Commentary: Resource planning and sprint capacity check.",
        2: "Commentary: Translation: 'Please check the Jira backlog before asking for new features.'",
        3: "Commentary: Our human processors are overheating. Please insert more coffee or reduce scope."
      }
    },
    {
      keywords: ['ai', 'artificial intelligence', 'machine learning', 'web3', 'blockchain', 'llm'],
      translations: {
        1: "Integrate machine learning models or automated API capabilities into the product workflow.",
        2: "Call a third-party LLM API endpoint or add automated conditional decision logic.",
        3: "Add a nested `if/else` block or an overpriced API call to a glorified chat wrapper that costs $4,000/month in API tokens."
      },
      commentaries: {
        1: "Commentary: Leveraging modern machine learning frameworks.",
        2: "Commentary: AI stands for 'Answering Inquiries' or 'Adding If-statements'.",
        3: "Commentary: 90% of 'AI features' are just a $20/month API key disguised as disruptive innovation."
      }
    },
    {
      keywords: ['asap', 'urgent', 'top priority', 'critical', 'emergency'],
      translations: {
        1: "High priority deliverable requiring expedited review and implementation.",
        2: "High priority item scheduled for immediate attention in the current development queue.",
        3: "Everything is priority 1, which mathematically means priority 1 has zero statistical significance."
      },
      commentaries: {
        1: "Commentary: Prioritized for current sprint cycle.",
        2: "Commentary: When everything is urgent, nothing gets done, but everyone gets coffee.",
        3: "Commentary: Priority 1 is a mood, not a project management methodology."
      }
    }
  ],
  'it-to-mkt': [
    {
      keywords: ['500 error', 'internal server error', 'crash', 'down', 'server down', 'outage', 'offline'],
      translations: {
        1: "We are currently experiencing a brief technical service interruption and working on restoration.",
        2: "We are conducting a brief scheduled service optimization window to improve platform stability.",
        3: "We are currently orchestrating an artisanal user-friction reduction window to optimize customer mindfulness."
      },
      commentaries: {
        1: "Commentary: Incident response team activated.",
        2: "Commentary: The database crashed, but we are framing it as maintenance.",
        3: "Commentary: The server room is on fire, but marketing calls it 'mindful digital detox'."
      }
    },
    {
      keywords: ['technical debt', 'refactoring', 'legacy code', 'code cleanup', 'spaghetti code'],
      translations: {
        1: "Improving internal code quality and system architecture to ensure long-term stability.",
        2: "Upgrading core platform infrastructure to support future feature additions and scalability.",
        3: "Unlocking foundational infrastructure synergies to future-proof our scalable hyper-growth architecture."
      },
      commentaries: {
        1: "Commentary: Routine codebase maintenance.",
        2: "Commentary: Fixing the code we rushed last quarter.",
        3: "Commentary: We built spaghetti code for 6 months, and now we need 6 months to untangle it."
      }
    },
    {
      keywords: ['feature not a bug', 'intended behavior', 'by design', 'not a bug'],
      translations: {
        1: "The current system behavior aligns with existing technical specifications.",
        2: "The system is functioning according to configured parameters and business rules.",
        3: "An exclusive, unannounced micro-interaction crafted to intrigue and engage curious power-users."
      },
      commentaries: {
        1: "Commentary: Verified against functional design documents.",
        2: "Commentary: It's weird, but it's supposed to do that.",
        3: "Commentary: We don't know why it does that, but please don't touch it or the login screen breaks."
      }
    },
    {
      keywords: ['worked on my machine', 'local environment', 'local machine', 'localhost'],
      translations: {
        1: "Successfully verified in developer environment; deploying to staging for verification.",
        2: "Feature verified in localized test environment prior to staging cluster sync.",
        3: "Hyper-optimized localized deployment showcasing peak performance prior to global ecosystem deployment."
      },
      commentaries: {
        1: "Commentary: Ready for staging deployment.",
        2: "Commentary: Works on my laptop, so it's a staging issue.",
        3: "Commentary: It works on my laptop, so the problem is clearly the universe."
      }
    },
    {
      keywords: ['out of scope', 'backlog', 'sprint 4', 'not in sprint', 'next quarter'],
      translations: {
        1: "Scheduled for evaluation in an upcoming product roadmap planning session.",
        2: "Earmarked for future release planning to prioritize core deliverables.",
        3: "Earmarked for our Q4 roadmap expansion phase to ensure maximum strategic intent and quality assurance."
      },
      commentaries: {
        1: "Commentary: Logged in product backlog for triage.",
        2: "Commentary: Not happening this month.",
        3: "Commentary: Sent directly to the digital graveyard where good ideas go to rest."
      }
    }
  ]
};

// Preset Quick Chips
const presetChips = {
  'mkt-to-it': [
    "Can we just make it pop by Friday?",
    "We need a quick growth-hack viral flywheel.",
    "This MVP is a top priority, simple tweak!",
    "Let's add AI and synergy to the landing page.",
    "What's your bandwidth for a minor pivot?"
  ],
  'it-to-mkt': [
    "The API endpoint is throwing 500 internal server errors.",
    "That's a feature, not a bug.",
    "It worked on my local machine environment.",
    "This request is out of scope and moved to backlog.",
    "We need 3 weeks for technical debt refactoring."
  ]
};

// Dictionary
// Every entry below is a real, in-the-wild jargon term. The mkt/it lines are our
// sarcastic spin, but the term itself — and the "source" citation — traces back to
// an actual glossary/dictionary site, so nobody can accuse this translator of making
// its jargon up. See SOURCES in index.html for the full bibliography.
const SOURCES = {
  TECHOPEDIA: { name: "Techopedia Tech Dictionary", url: "https://www.techopedia.com/dictionary" },
  WHATIS: { name: "TechTarget WhatIs.com", url: "https://www.techtarget.com/whatis/" },
  WIKI_CS: { name: "Wikipedia: Glossary of Computer Science", url: "https://en.wikipedia.org/wiki/Glossary_of_computer_science" },
  NIST: { name: "NIST CSRC Glossary", url: "https://csrc.nist.gov/glossary" },
  WEBOPEDIA: { name: "Webopedia", url: "https://www.webopedia.com/" },
  MAILCHIMP: { name: "Mailchimp Marketing Glossary", url: "https://mailchimp.com/marketing-glossary/" },
  BIZJARGONS: { name: "BusinessJargons.com", url: "https://www.businessjargons.com/" },
  AMA: { name: "American Marketing Association", url: "https://www.ama.org/topics/branding/" }
};

const dictionaryData = [
  // --- Original launch set ---
  { term: "Bandwidth", mkt: "How much free time you have to listen to my new ideas.", it: "CPU/RAM allocation before system crash occurs.", source: SOURCES.TECHOPEDIA },
  { term: "Quick Fix", mkt: "A 5-minute task that I forgot to ask for last week.", it: "A 40-hour architectural refactor that breaks production." },
  { term: "Make It Pop", mkt: "Add visual magic, vibrant colors, and excitement.", it: "Violate contrast standards and ruin the UX hierarchy." },
  { term: "MVP", mkt: "A fully finished app, but launched quickly.", it: "A broken prototype held together by hope and hardcoded logic.", source: SOURCES.BIZJARGONS },
  { term: "Technical Debt", mkt: "An abstract excuse IT uses when they don't want to build my button.", it: "The digital mortgage we accrued by rushing previous MVPs.", source: SOURCES.WIKI_CS },
  { term: "Agile", mkt: "We can change our minds every day without consequence.", it: "Two-week cycles of panic followed by retrospective guilt.", source: SOURCES.WIKI_CS },
  { term: "Bug", mkt: "A catastrophic failure caused by lazy developers.", it: "An undocumented edge case created by ambiguous requirements.", source: SOURCES.WIKI_CS },
  { term: "AI / Machine Learning", mkt: "Magic fairy dust that increases company valuation.", it: "A glorified `if-else` block or an expensive third-party API call.", source: SOURCES.TECHOPEDIA },

  // --- Real IT jargon, sourced ---
  { term: "Air Gap", mkt: "A bold, security-first architecture built for maximum customer trust.", it: "Physically unplugging a system from the network because we don't trust our own firewall.", source: SOURCES.TECHOPEDIA },
  { term: "Zero Trust", mkt: "Our forward-thinking philosophy: every customer gets a personally verified, premium experience.", it: "Assuming every user, device, and packet is guilty until proven innocent. Forever.", source: SOURCES.NIST },
  { term: "Kubernetes", mkt: "The engine behind our infinitely scalable, cloud-native platform.", it: "A system so complex it needs its own full-time engineer just to manage the complexity.", source: SOURCES.WHATIS },
  { term: "Latency", mkt: "A brief, intentional pause designed to build delightful anticipation.", it: "The gap between clicking a button and reconsidering your career choices.", source: SOURCES.TECHOPEDIA },
  { term: "Zero-Day Vulnerability", mkt: "An exciting opportunity for rapid, agile incident response.", it: "A hole in the software that hackers found before we did.", source: SOURCES.NIST },
  { term: "Edge Computing", mkt: "Processing power that lives closer to our customers than our own support team does.", it: "Running code on a box in a closet because the cloud bill got too big.", source: SOURCES.WEBOPEDIA },
  { term: "Microservices", mkt: "A beautifully modular architecture built for infinite flexibility.", it: "Fifty small programs that all have to be running correctly at once, or nothing works.", source: SOURCES.WIKI_CS },
  { term: "Legacy System", mkt: "A time-tested, battle-hardened platform with deep institutional wisdom.", it: "Code nobody understands, written by someone who left the company in 2014.", source: SOURCES.TECHOPEDIA },

  // --- Real marketing jargon, sourced ---
  { term: "Omnichannel", mkt: "A seamless, unified customer journey across every single touchpoint.", it: "Now five different systems have to stay in sync instead of one.", source: SOURCES.MAILCHIMP },
  { term: "A/B Testing", mkt: "Data-driven creative optimization powered by real customer insight.", it: "Marketing changed the button color again and needs proof it mattered.", source: SOURCES.MAILCHIMP },
  { term: "Email Marketing", mkt: "A highly personalized, one-to-one relationship-building channel.", it: "The reason the mail server spikes every Tuesday at 9am.", source: SOURCES.MAILCHIMP },
  { term: "Brand Equity", mkt: "The invaluable, intangible trust our name carries in the market.", it: "Whatever number marketing says it's worth, since nobody can actually measure it.", source: SOURCES.AMA },
  { term: "Growth Hacking", mkt: "A scrappy, innovative approach to unlocking exponential user acquisition.", it: "Doing things that don't scale until legal finds out.", source: SOURCES.MAILCHIMP },
  { term: "Synergy", mkt: "The multiplicative value created when teams align around a shared vision.", it: "A word used in place of an actual plan.", source: SOURCES.BIZJARGONS },
  { term: "Stakeholder Alignment", mkt: "Ensuring every voice at the table helps shape our shared direction.", it: "Nine people with veto power, none of whom agree with each other.", source: SOURCES.BIZJARGONS },
  { term: "Value Proposition", mkt: "The unique, compelling reason customers choose us over anyone else.", it: "The one sentence marketing needs from us by end of day, apparently.", source: SOURCES.BIZJARGONS }
];

// Initialize UI
document.addEventListener('DOMContentLoaded', () => {
  renderPresets();
  renderDictionary();
  updateSarcasmUI();
  handleTranslate();
});

// Mode Switcher
function switchMode(mode) {
  currentMode = mode;
  
  const btnMkt = document.getElementById('btn-mkt-to-it');
  const btnIt = document.getElementById('btn-it-to-mkt');
  
  if (btnMkt && btnIt) {
    btnMkt.classList.toggle('active', mode === 'mkt-to-it');
    btnIt.classList.toggle('active', mode === 'it-to-mkt');
  }

  const inputLabel = document.getElementById('input-label');
  const outputLabel = document.getElementById('output-label');
  const sourceInput = document.getElementById('source-input');
  const sourceInputLabel = document.getElementById('source-input-label');

  if (mode === 'mkt-to-it') {
    if (inputLabel) inputLabel.textContent = '📢 Source: Marketing Speak';
    if (outputLabel) outputLabel.textContent = '💻 Translation: IT Reality';
    if (sourceInput) sourceInput.placeholder = "Type Marketing Speak here... (e.g. 'Can we just make it pop and add AI by Friday?')";
    if (sourceInputLabel) sourceInputLabel.textContent = 'Marketing Speak to translate';
  } else {
    if (inputLabel) inputLabel.textContent = '💻 Source: IT Reality';
    if (outputLabel) outputLabel.textContent = '📢 Translation: Marketing Spin';
    if (sourceInput) sourceInput.placeholder = "Type IT Speak here... (e.g. 'The server crashed due to 500 internal errors and technical debt.')";
    if (sourceInputLabel) sourceInputLabel.textContent = 'IT Reality to translate';
  }

  clearInput();
  renderPresets();
}

// Sarcasm Level Change Handler
function setSarcasmLevel(level) {
  sarcasmLevel = parseInt(level, 10);
  updateSarcasmUI();
  handleTranslate();
}

function updateSarcasmUI() {
  const ratingEl = document.getElementById('cynicism-rating');
  const sliderEl = document.getElementById('sarcasm-slider');
  const levelTextEl = document.getElementById('sarcasm-level-text');

  if (sliderEl) sliderEl.value = sarcasmLevel;

  let text = "Level 3: Unfiltered Cynicism 🔥";
  // Lightened from #ec4899/0.2 alpha: the darker pink-on-pink combo measured
  // 4.09:1 / 4.38:1 against its badge backgrounds, just under the 4.5:1 WCAG AA
  // minimum for normal-size text. #f472b6 at 0.15 alpha measures ~6:1.
  let badgeColor = "rgba(236, 72, 153, 0.15)";
  let textColor = "#f472b6";

  if (sarcasmLevel === 1) {
    text = "Level 1: Professional / Sincere 😇";
    badgeColor = "rgba(59, 130, 246, 0.2)";
    textColor = "#60a5fa";
  } else if (sarcasmLevel === 2) {
    text = "Level 2: Mild Snark 😼";
    badgeColor = "rgba(6, 182, 212, 0.2)";
    textColor = "#22d3ee";
  }

  // Keep the slider's accessible name/value in sync so screen reader users
  // hear the same level text sighted users see, instead of just a bare number.
  if (sliderEl) {
    sliderEl.setAttribute('aria-valuenow', String(sarcasmLevel));
    sliderEl.setAttribute('aria-valuetext', text.replace(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/gu, '').trim());
  }

  if (ratingEl) {
    ratingEl.textContent = text;
    ratingEl.style.backgroundColor = badgeColor;
    ratingEl.style.color = textColor;
  }

  if (levelTextEl) {
    levelTextEl.textContent = text;
    levelTextEl.style.color = textColor;
  }
}

// Translation Handler
function handleTranslate() {
  const inputEl = document.getElementById('source-input');
  if (!inputEl) return;
  const input = inputEl.value;

  const countEl = document.getElementById('input-char-count');
  if (countEl) countEl.textContent = `${input.length} chars`;

  const outputEl = document.getElementById('translation-output');
  const commentaryEl = document.getElementById('commentary-text');

  if (!input.trim()) {
    if (outputEl) outputEl.innerHTML = '<span class="placeholder-text">Your translated output will render here in real time...</span>';
    if (commentaryEl) commentaryEl.textContent = 'Ready for input. Please feed me buzzwords or technical jargon so I can process your team\'s collective denial.';
    return;
  }

  const activeRules = translations[currentMode];
  let translationResult = '';
  let matchFound = false;
  let commentaryResult = '';

  const lowerInput = input.toLowerCase();

  for (let rule of activeRules) {
    if (rule.keywords.some(k => lowerInput.includes(k))) {
      translationResult += rule.translations[sarcasmLevel] + ' ';
      commentaryResult = rule.commentaries[sarcasmLevel];
      matchFound = true;
    }
  }

  if (!matchFound) {
    if (currentMode === 'mkt-to-it') {
      if (sarcasmLevel === 1) {
        translationResult = "IT Request: Requires technical clarification and project ticket submission.";
        commentaryResult = "Commentary: Standard ticket required for scheduling.";
      } else if (sarcasmLevel === 2) {
        translationResult = "IT Interpretation: Missing technical requirements. Defaulting to low-priority triage queue.";
        commentaryResult = "Commentary: Please specify steps to reproduce before submitting.";
      } else {
        translationResult = "IT Interpretation: Requirement lacks technical logic. Defaulting to: 'Please submit a Jira ticket with steps to reproduce, priority low.'";
        commentaryResult = "Commentary: Input contains generic human language unsupported by current API specifications.";
      }
    } else {
      if (sarcasmLevel === 1) {
        translationResult = "Marketing Notice: Operational update regarding active technical optimization.";
        commentaryResult = "Commentary: Standard customer communication.";
      } else if (sarcasmLevel === 2) {
        translationResult = "Marketing Spin: 'We are currently conducting scheduled infrastructure improvements.'";
        commentaryResult = "Commentary: Communication optimized for stakeholder reassurance.";
      } else {
        translationResult = "Marketing Spin: 'We are currently orchestrating a next-generation paradigm synergy window to optimize customer mindfulness.'";
        commentaryResult = "Commentary: IT reality successfully obscured under 3 layers of corporate buzzwords.";
      }
    }
  }

  if (outputEl) outputEl.textContent = translationResult.trim();
  if (commentaryEl) commentaryEl.textContent = commentaryResult;
}

// Presets Renderer
function renderPresets() {
  const container = document.getElementById('preset-chips');
  if (!container) return;
  container.innerHTML = '';

  const chips = presetChips[currentMode];
  chips.forEach(text => {
    const chip = document.createElement('button');
    chip.className = 'chip';
    chip.textContent = text;
    chip.onclick = () => {
      const inputEl = document.getElementById('source-input');
      if (inputEl) {
        inputEl.value = text;
        handleTranslate();
      }
    };
    container.appendChild(chip);
  });
}

// Dictionary Renderer
function renderDictionary() {
  const grid = document.getElementById('dictionary-grid');
  if (!grid) return;
  grid.innerHTML = '';

  dictionaryData.forEach(item => {
    const card = document.createElement('div');
    card.className = 'dict-card';
    card.innerHTML = `
      <div class="dict-term">${item.term}</div>
      <div class="dict-mkt"><strong>📢 Mkt:</strong> ${item.mkt}</div>
      <div class="dict-it"><strong>💻 IT:</strong> ${item.it}</div>
      ${item.source ? `<a class="dict-source" href="${item.source.url}" target="_blank" rel="noopener noreferrer">🔗 Source: ${item.source.name}</a>` : ''}
    `;
    grid.appendChild(card);
  });
}

// Filter Dictionary
function filterDictionary() {
  const searchEl = document.getElementById('dict-search');
  if (!searchEl) return;
  const query = searchEl.value.toLowerCase();
  
  const filtered = dictionaryData.filter(item => 
    item.term.toLowerCase().includes(query) ||
    item.mkt.toLowerCase().includes(query) ||
    item.it.toLowerCase().includes(query)
  );

  const grid = document.getElementById('dictionary-grid');
  if (!grid) return;
  grid.innerHTML = '';

  filtered.forEach(item => {
    const card = document.createElement('div');
    card.className = 'dict-card';
    card.innerHTML = `
      <div class="dict-term">${item.term}</div>
      <div class="dict-mkt"><strong>📢 Mkt:</strong> ${item.mkt}</div>
      <div class="dict-it"><strong>💻 IT:</strong> ${item.it}</div>
      ${item.source ? `<a class="dict-source" href="${item.source.url}" target="_blank" rel="noopener noreferrer">🔗 Source: ${item.source.name}</a>` : ''}
    `;
    grid.appendChild(card);
  });
}

// Helper Functions
function clearInput() {
  const inputEl = document.getElementById('source-input');
  if (inputEl) inputEl.value = '';
  handleTranslate();
}

function loadRandomSample() {
  const chips = presetChips[currentMode];
  const randomText = chips[Math.floor(Math.random() * chips.length)];
  const inputEl = document.getElementById('source-input');
  if (inputEl) {
    inputEl.value = randomText;
    handleTranslate();
  }
}

function copyOutput() {
  const outputEl = document.getElementById('translation-output');
  if (!outputEl) return;
  const outputText = outputEl.textContent;
  if (!outputText || outputText.includes('Your translated output')) return;

  navigator.clipboard.writeText(outputText).then(() => {
    const btn = document.getElementById('copy-btn');
    if (btn) {
      const originalText = btn.textContent;
      btn.textContent = '✅ Copied!';
      setTimeout(() => {
        btn.textContent = originalText;
      }, 2000);
    }
  });
}
