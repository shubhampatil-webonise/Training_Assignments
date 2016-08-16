function setItemInStorage(obj, key, value){ 
	function wrapper(key, value){ 
		this.setItem(key, value);
	}
	
	wrapper.call(obj, key, value);

	//var binder = wrapper.bind(obj);
	//binder(key, value);

	return 'Done'
}

function getItemFromStorage(obj, key){ 
	function wrapper(key){ 
		return this.getItem(key);
	}

	return wrapper.call(obj, key);

	//var binder = wrapper.bind(obj);
	//return binder(key);
}

function printLengthOfStorage(obj){
	function wrapper(){
		return this.length;
	}

	return wrapper.call(obj);

	//var binder = wrapper.bind(obj);
	//return binder();
}

function clearStorage(obj){
	function wrapper(){
		return this.clear;
	}

	return wrapper.call(obj);

	//var binder = wrapper.bind(obj);
	//return binder();
}
