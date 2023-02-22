// Define the residents variable and assign it an empty array
let residents = [];

// Call the getResidents() function to populate the residents array
getResidents();

// Function to get the list of residents
function getResidents() {
    // Make a GET request to the server to get the list of residents
    fetch('/api/residents/')
        .then(response => response.json())
        .then(data => {
            // Add each resident to the residents array
            for (let i = 0; i < data.length; i++) {
                residents.push(data[i]);
            }
        })
        .catch(error => console.error(error));
}

// Function to add a new resident to the list
function addResident(resident) {
    // Make a POST request to the server to add the new resident
    fetch('/api/residents/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(resident)
    })
        .then(response => response.json())
        .then(data => {
            // Add the new resident to the residents array
            residents.push(data);
        })
        .catch(error => console.error(error));
}

// Function to update an existing resident
function updateResident(resident) {
    // Make a PUT request to the server to update the resident
    fetch(`/api/residents/${resident.id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(resident)
    })
        .then(response => response.json())
        .then(data => {
            // Find the index of the updated resident in the residents array
            const index = residents.findIndex(r => r.id === data.id);
            // Replace the old resident with the updated one
            residents.splice(index, 1, data);
        })
        .catch(error => console.error(error));
}

// Function to delete a resident
function deleteResident(residentId) {
    // Make a DELETE request to the server to delete the resident
    fetch(`/api/residents/${residentId}/`, {
        method: 'DELETE'
    })
        .then(() => {
            // Find the index of the deleted resident in the residents array
            const index = residents.findIndex(r => r.id === residentId);
            // Remove the deleted resident from the residents array
            residents.splice(index, 1);
        })
        .catch(error => console.error(error));
}
