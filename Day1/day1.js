const fs = require('fs')

fs.readFile('input.txt', (err, data) => {
	if (err) throw err;
	let nums = data.toString().split('\n');
	nums.map(parseInt);

	let counter = 1;
	for (let i = 0, n = nums.length - 2; i < n; i++) {
		if (nums[i + 1] > nums[i]) {
			counter++;
		}	
	}

	console.log(counter);
});
