import codecs

# Read the data from shayari_new.js
with codecs.open('shayari_new.js', 'r', 'utf-8') as f:
    data_content = f.read()

# App functions code
app_functions = '''

// App State
let currentIndex = 0;
let filteredShayari = [...shayariData];
let favorites = JSON.parse(localStorage.getItem('ulfat-favorites') || '[]');
let selectedFilters = {
    language: null,
    category: null
};

// Initialize App
function init() {
    createFilters();
    updateUI();
    updateCounter();
    updateFavCount();
    setupSearch();
}

// Create Filter Buttons
function createFilters() {
    const filtersDiv = document.getElementById('filters');
    
    const languages = ['सभी', 'हिंदी', 'اردو', 'मराठी'];
    const categories = ['सभी', 'रोमांटिक', 'दुःख', 'फिलोसफी', 'भक्ति'];
    
    languages.forEach(lang => {
        const btn = document.createElement('button');
        btn.className = 'filter-btn';
        btn.textContent = lang;
        btn.onclick = () => filterByLanguage(lang);
        filtersDiv.appendChild(btn);
    });
    
    categories.forEach(cat => {
        const btn = document.createElement('button');
        btn.className = 'filter-btn';
        btn.textContent = cat;
        btn.onclick = () => filterByCategory(cat);
        filtersDiv.appendChild(btn);
    });
}

// Filter Functions
function filterByLanguage(lang) {
    const langMap = {'हिंदी': 'hindi', 'اردو': 'urdu', 'मराठी': 'marathi', 'सभी': null};
    selectedFilters.language = langMap[lang];
    applyFilters();
}

function filterByCategory(cat) {
    const catMap = {'रोमांटिक': 'romantic', 'दुःख': 'sad', 'फिलोसफी': 'philosophical', 'भक्ति': 'devotional', 'सभी': null};
    selectedFilters.category = catMap[cat];
    applyFilters();
}

function applyFilters() {
    filteredShayari = shayariData.filter(item => {
        const langMatch = !selectedFilters.language || item.language === selectedFilters.language;
        const catMatch = !selectedFilters.category || item.category === selectedFilters.category;
        return langMatch && catMatch;
    });
    
    currentIndex = 0;
    updateUI();
    updateCounter();
}

// Search Function
function setupSearch() {
    const searchBox = document.getElementById('searchBox');
    searchBox.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        if (query) {
            filteredShayari = shayariData.filter(item => 
                item.text.toLowerCase().includes(query) || 
                item.author.toLowerCase().includes(query)
            );
        } else {
            applyFilters();
        }
        currentIndex = 0;
        updateUI();
        updateCounter();
    });
}

// Update UI
function updateUI() {
    if (filteredShayari.length === 0) {
        document.getElementById('shayariText').textContent = 'कोई शायरी नहीं मिली';
        document.getElementById('author').textContent = '';
        return;
    }
    
    const current = filteredShayari[currentIndex];
    document.getElementById('shayariText').textContent = current.text;
    document.getElementById('author').textContent = `- ${current.author}`;
    
    document.getElementById('prevBtn').disabled = currentIndex === 0;
    document.getElementById('nextBtn').disabled = currentIndex === filteredShayari.length - 1;
    
    updateFavIcon();
}

function updateCounter() {
    document.getElementById('counter').textContent = 
        ` ${currentIndex + 1} / ${filteredShayari.length} (कुल: ${shayariData.length})`;
}

// Navigation
function nextShayari() {
    if (currentIndex < filteredShayari.length - 1) {
        currentIndex++;
        updateUI();
        updateCounter();
    }
}

function prevShayari() {
    if (currentIndex > 0) {
        currentIndex--;
        updateUI();
        updateCounter();
    }
}

function randomShayari() {
    currentIndex = Math.floor(Math.random() * filteredShayari.length);
    updateUI();
    updateCounter();
}

// Favorites
function toggleFavorite() {
    const current = filteredShayari[currentIndex];
    const index = favorites.indexOf(current.id);
    
    if (index > -1) {
        favorites.splice(index, 1);
    } else {
        favorites.push(current.id);
    }
    
    localStorage.setItem('ulfat-favorites', JSON.stringify(favorites));
    updateFavIcon();
    updateFavCount();
}

function updateFavIcon() {
    const current = filteredShayari[currentIndex];
    const isFav = favorites.includes(current.id);
    document.getElementById('favIcon').textContent = isFav ? '❤️' : '🤍';
}

function updateFavCount() {
    document.getElementById('favCount').textContent = favorites.length;
}

function showFavorites() {
    const modal = document.getElementById('favoritesModal');
    const list = document.getElementById('favoritesList');
    
    const favShayari = shayariData.filter(item => favorites.includes(item.id));
    
    if (favShayari.length === 0) {
        list.innerHTML = '<p style="text-align:center; color:#999;">कोई पसंदीदा शायरी नहीं है</p>';
    } else {
        list.innerHTML = favShayari.map(item => `
            <div style="background:#f5f5f5; padding:15px; margin:10px 0; border-radius:10px; cursor:pointer;" 
                 onclick="goToShayari(${item.id})">
                <p style="font-size:16px; line-height:1.6;">${item.text.substring(0, 80)}...</p>
                <p style="color:#8B4789; font-style:italic; margin-top:5px;">- ${item.author}</p>
            </div>
        `).join('');
    }
    
    modal.classList.add('active');
}

function closeFavorites() {
    document.getElementById('favoritesModal').classList.remove('active');
}

function goToShayari(id) {
    closeFavorites();
    currentIndex = filteredShayari.findIndex(item => item.id === id);
    if (currentIndex === -1) currentIndex = 0;
    updateUI();
    updateCounter();
}

// Share & Copy
function shareShayari() {
    const current = filteredShayari[currentIndex];
    const text = `${current.text}\\n\\n- ${current.author}\\n\\nशायर किया गया उल्फ़त ऐप से`;
    
    if (navigator.share) {
        navigator.share({
            title: 'उल्फ़त - Shayari',
            text: text
        });
    } else {
        copyToClipboard(text);
        alert('शायरी कॉपी हो गई है! 📋');
    }
}

function copyShayari() {
    const current = filteredShayari[currentIndex];
    const text = `${current.text}\\n\\n- ${current.author}`;
    copyToClipboard(text);
    alert('शायरी कॉपी हो गई है! 📋');
}

function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
}

// Start App
init();
'''

# Write the final file
with codecs.open('shayari.js', 'w', 'utf-8') as f:
    f.write(data_content)
    f.write(app_functions)

print("✅ Successfully created shayari.js with:")
print("   - Hindi Shayari section")
print("   - Urdu Shayari section")
print("   - Marathi Shayari section")
print("   - Combined shayariData array")
print("   - All app functions")
