let requestButton = document.getElementById("submit")
let picdiv = document.getElementById("picture")
let contain = document.getElementById("pic-contain")
let form = document.getElementById("form")

requestButton.addEventListener("click", evt => {

  picdiv.style.display = "block"
  contain.style.display = "block"

  let form = document.getElementById("form")
  character = form.elements[0].value.toString().trim().toLowerCase()
  //form.reset()

  superagent.post('http://127.0.0.1:5000/')
  .send({'character' : character})
  .set('accept', 'json')
  .end(function (err, res) {
    console.log(res)
    picdiv.innerHTML = `<h3>Character: ${res.body.name}</h3><br><br><img class="resized" src="${res.body.image}" alt="${res.name}"/>`
  })
})
