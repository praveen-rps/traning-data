function fetchData(){
    return new Promise( (resolve,reject) =>{
        console.log("Data is fetching...!");
        setTimeout(
            ()=>{
                const success = false;
                if(success)
                    resolve({id:1001,name:'kumar'})
                else{
                    reject("Error fetching data");
                }
            },3000);
        }
   );
}



fetchData()
.then(
    result => {
        console.log("Data Received : ", result)
    })
.catch(error => {
    console.log("Error -->", error)
})


