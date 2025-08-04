
async function fetchUser(userId){
    try{
        console.log("Fetching Started..!")
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/1`)
       if( !response.ok)
        throw new Error("Error:"+(response.status))
       else{
        const user =  await response.json();
        console.log(`${user.id} => ${user.name}`);
       }
    }
    catch(err){
        console.error(err.message)
    }
}

fetchUser(1);