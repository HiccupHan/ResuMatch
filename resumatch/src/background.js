//inject script into every webpage
var tabToUrl = {};
const urlRegex = /http:\/\/localhost:8501/;
chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  if (changeInfo.status == 'complete') {
    chrome.scripting.executeScript({
      files: ['injectedScript.js'],
      target: { tabId: tab.id }
    });
    tabToUrl[tabId] = tab.url;
  }
});

chrome.tabs.onRemoved.addListener(function (tabId, info) {
  if (urlRegex.test(tabToUrl[tabId])) {
    const request = new Request('http://localhost:8000/resume_names', { method: 'POST' });
    fetch(request)
      .then((response) => response.json())
      .then((data) => {
        chrome.storage.local.set({ 'storedResumes': data });
        console.log(data);
      });
  }
  delete tabToUrl[tabId];
})
