chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab){
  if(changeInfo.status == 'complete'){
    chrome.scripting.executeScript({
      files: ['injectedScript.js'],
      target: {tabId: tab.id}
    });
  }  
  });
