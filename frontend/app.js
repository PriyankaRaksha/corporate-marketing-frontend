fetch("/campaigns")
  .then(res => res.json())
  .then(data => {
    document.getElementById("data").innerText = data.length;
  });