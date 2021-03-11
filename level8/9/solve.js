function fireEvent(key) {
	var evt = new KeyboardEvent('keyup', {'keyCode':key, 'which':key})
	document.body.dispatchEvent(evt);
}

[38,38,40,40,37,39,37,39,66,65].map(key => fireEvent(key))
