const cupcakeList = document.getElementById('cupcakes')
const newButton = document.getElementById('newBtn')

async function retrieveAllCupcakes(){
    let allCupcakes = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    console.log(allCupcakes.data.cupcakes)
    cupcakeList.innerHTML = '';
    for (let cupcake of allCupcakes.data.cupcakes){
        console.log(cupcake)
        const cupcakeLI = document.createElement('li')
        cupcakeLI.innerText = `Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating = ${cupcake.rating}`
        cupcakeList.appendChild(cupcakeLI)
    }
   
}

retrieveAllCupcakes();

const create = async function createNewCupcake(e){
    e.preventDefault()
    const addForm = document.getElementById('addForm')
    let values = addForm.querySelectorAll('input')
    console.log(values)

    let resp = await axios.post('http://127.0.0.1:5000/api/cupcakes', json = {
        'flavor': values[0].value,
        'size': values[1].value,
        'rating': values[2].value
    })
    retrieveAllCupcakes()
    cupcakeList.appendChild()
    return resp
}


newButton.addEventListener('click', function(){
    const addForm = document.createElement('form')
    addForm.id = 'addForm'
    const flavInput = document.createElement('input')
    flavInput.placeholder = 'Flavor'
    const sizeInput  = document.createElement('input')
    sizeInput.placeholder = 'Size'
    const ratingInput = document.createElement('input')
    ratingInput.placeholder = 'Rating'
    const submitBtn = document.createElement('button')
    submitBtn.id = 'submit'
    submitBtn.innerText = 'submit'
    addForm.appendChild(flavInput)
    addForm.appendChild(sizeInput)
    addForm.appendChild(ratingInput)
    addForm.appendChild(submitBtn)
    document.body.appendChild(addForm)

    submitBtn.addEventListener('click', create)
})


