const fs = require('fs');
const content = fs.readFileSync('c:\\Ulfat\\shayari.js', 'utf8');
eval(content);

console.log('Total hindiShayari:', hindiShayari.length);
console.log('Total shayariData:', shayariData.length);
console.log('\nChecking index 1651 in shayariData:');
console.log('Item at 1651:', shayariData[1651]);
console.log('\nChecking around index 1651:');
for (let i = 1648; i <= 1654; i++) {
  const item = shayariData[i];
  if (!item || typeof item !== 'object') {
    console.log(`⚠️ Index ${i}: UNDEFINED or INVALID`);
  } else {
    console.log(`✅ Index ${i}: id=${item.id}, lang=${item.language}, cat=${item.category}`);
  }
}

// Find all undefined entries
console.log('\n🔍 Searching for all undefined entries:');
let count = 0;
shayariData.forEach((item, index) => {
  if (!item || typeof item !== 'object') {
    console.log(`⚠️ Undefined at index ${index}`);
    count++;
  }
});
console.log(`\nTotal undefined entries: ${count}`);
