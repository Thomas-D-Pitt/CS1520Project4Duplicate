export function process_all_teams(func) {
	fetch('/teams/', {
		method: "get",
		headers: { "Content-type": "application/json" },
	  })
	  .then((response) => {
		return response.json();
	  })
	  .then((result) => {
		var promises = []
		var teams = []
		for (let i = 0; i < result.length; i++){
			let newPromise = new Promise (function(myResolve, myReject) {
					fetch(`/teams/${result[i]}`, {
					method: "get",
					headers: { "Content-type": "application/json" },
				})
				.then((response) => {
					return response.json();
				})
				.then((result) => {
					teams[i] = (result)
					myResolve()
				})
			})
			promises[i] = newPromise
		}
		Promise.all(promises).then(() => {
			console.log(js_avg_goals)
			func(teams)
		})
		
	  });
}

export function js_avg_goals(teams) {
	let largestAvg = null
	for (var i = 0; i < teams.length; i++){
		let sum = 0
		for (var j = 0; j < teams[i].players.length; j++){
			sum += teams[i].players[j].goals
		}
		sum /= teams[i].players.length
		teams[i].averageScore = sum
		if (largestAvg == null || largestAvg.averageScore < sum){
			largestAvg = teams[i]
		}
		  
	}
	console.log( `Team with largest average is ${largestAvg.name} with average score: ${largestAvg.averageScore}` )
	
	
}
