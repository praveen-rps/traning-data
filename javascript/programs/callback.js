function fetchData(callback){
    console.log("Fetching data....!")
    setTimeout(()=>{
            const data = {id:1001, name:'Kumar'};
            callback(data);
    }, 5000);
}

fetchData(function(result){
    console.log("Data Received ",result)
});