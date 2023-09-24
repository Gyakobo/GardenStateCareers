const checkIfUserExists = (event) => {
    const emailFormElement = event.target;
    const email = event.target.value;

    axios.post('/validate-user', {
        email: email
    })
        .then((response) => {
            if (response.data.user_exists == "true") {
                console.log("User exists");
            }
            else console.log("User doesn't exist");
        }, (error) => {
            console.log("Error");
        });

}



