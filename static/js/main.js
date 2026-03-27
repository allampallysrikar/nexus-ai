document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const charCount = document.getElementById('count');
    const analyzeBtn = document.getElementById('analyze-btn');
    const loading = document.getElementById('loading');
    const resultsSection = document.getElementById('results');
    const targetLangSelect = document.getElementById('target-lang');

    // UI Elements for Results
    const enTransResult = document.getElementById('en-trans-result');
    const targetTransResult = document.getElementById('target-trans-result');
    const summaryResult = document.getElementById('summary-result');
    const sentimentLabel = document.getElementById('sentiment-label');
    const sentimentBar = document.getElementById('sentiment-bar');
    const sentimentScore = document.getElementById('sentiment-score');
    const entitiesContainer = document.getElementById('entities-container');

    // Tab Navigation
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const target = btn.getAttribute('data-target');
            document.getElementById(target).classList.add('active');
        });
    });

    // Character Count functionality
    textInput.addEventListener('input', () => {
        charCount.textContent = textInput.value.length;
    });

    analyzeBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        const targetLanguage = targetLangSelect.value;

        if (!text) {
            alert('Please enter some text to analyze.');
            textInput.focus();
            return;
        }

        // UI State: Loading
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<span>Processing...</span> <i class="fa-solid fa-spinner fa-spin"></i>';
        resultsSection.classList.add('hidden');
        loading.classList.remove('hidden');

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 
                    text: text,
                    targetLanguage: targetLanguage,
                    task: 'all' 
                })
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.error || 'Server error occurred');
            }

            const data = await response.json();
            
            // Populate Translations
            enTransResult.textContent = data.english_translation;
            targetTransResult.textContent = data.target_translation;

            // Populate Sentiment
            if (data.sentiment) {
                const sentiment = data.sentiment;
                sentimentLabel.textContent = sentiment.label;
                sentimentLabel.className = ''; 
                
                // Sanitize label for CSS class name
                const safeLabel = sentiment.label.replace(/[^a-zA-Z0-9]/g, '-').toLowerCase();
                sentimentLabel.classList.add(`sentiment-${safeLabel}`);
                
                sentimentScore.textContent = sentiment.score;
                sentimentBar.style.width = `${Math.min(sentiment.score * 100, 100)}%`;
                
                if(sentiment.label === 'POSITIVE') sentimentBar.style.backgroundColor = 'var(--success)';
                else if(sentiment.label === 'NEGATIVE') sentimentBar.style.backgroundColor = 'var(--danger)';
                else sentimentBar.style.backgroundColor = 'var(--warning)';
            }

            // Populate Summary
            if (data.summary) {
                summaryResult.textContent = data.summary;
            }

            // Populate Entities
            entitiesContainer.innerHTML = '';
            if (data.entities && data.entities.length > 0) {
                data.entities.forEach(entity => {
                    const tag = document.createElement('div');
                    let entityType = entity.entity.replace('B-', '').replace('I-', '');
                    tag.className = `entity-tag entity-${entityType}`;
                    tag.innerHTML = `
                        <span class="entity-type">${entityType}</span>
                        <span class="entity-word">${entity.word}</span>
                    `;
                    entitiesContainer.appendChild(tag);
                });
            } else {
                entitiesContainer.innerHTML = '<p class="text-muted">No specific entities found in the text.</p>';
            }

            // Restore UI State
            loading.classList.add('hidden');
            resultsSection.classList.remove('hidden');
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        } catch (error) {
            alert(`Analysis failed: ${error.message}`);
            loading.classList.add('hidden');
        } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.innerHTML = '<span>Analyze Text</span> <i class="fa-solid fa-wand-magic-sparkles"></i>';
        }
    });
});
