const fitCSVDataToForm = (data) => {
  // loop through data and create new array of objects
  let newData = [];
  for (let el of data) {
    // change data to fit form
    let newObj = {
      name: `${el["Buyer first name"]} ${el["Buyer last name"]}`,
      address1: el["Shipping address 1"],
      address2: el["Shipping address 2"],
      city: el["Shipping city"],
      state: el["Shipping state"],
      zip: el["Shipping zip"],
      country: el["Shipping country"],
    };
    newData.push(newObj);
  }
  return newData;
};

const postData = async (request) => {
  let response = await fetch("/print/", {
    method: "POST",
    redirect: "follow",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ addresses: request }),
  });
  if (response.ok) {
    window.location.href = "/print/";
  }
  return response.json();
};

const handleData = (data) => {
  let request = fitCSVDataToForm(data);
  //console.log(request);
  return postData(request);
};
window.addEventListener("load", () => {
  // Access the uploader and form elements...
  const uploader = document.getElementById("uploader");
  const form = document.getElementById("form");

  // ...and take over its submit event.
  uploader.addEventListener("submit", (event) => {
    event.preventDefault();

    /** @type {File} */
    const file = document.getElementById("file").files[0];

    // Validate type is text/csv
    if (file.type !== "text/csv") {
      alert("File must be a CSV");
      return;
    }

    Papa.parse(file, {
      header: true,
      complete: async (results) => {
        alert(await handleData(results.data));
      },
    });
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    // from the form, get name, address1, address2, city, state, zip, country
    let name = document.getElementById("name").value;
    let address1 = document.getElementById("address1").value;
    let address2 = document.getElementById("address2").value;
    let city = document.getElementById("city").value;
    let state = document.getElementById("state").value;
    let zip = document.getElementById("zip").value;
    let country = document.getElementById("country").value;

    // create array of length 1 with the data
    let data = [
      {
        name,
        address1,
        address2,
        city,
        state,
        zip,
        country,
      },
    ];

    handleData(data);
  });
});
