let x = document.querySelectorAll('.indecator input');
let y = document.querySelectorAll('.indecator label');

const calculateReating = (text) =>{
    return ((text[0]*1 + text[1]*1 + text[2]*1)/3).toFixed(1)
}

for(let i=0; i<x.length; i++){
    let z =  calculateReating(x[i].value.split(','));
    if(z < 5){
        y[i].style.backgroundColor = '#ff4c4c';
        y[i].textContent = z;
    }
    else if(z >= 5 && z< 8){
        y[i].style.backgroundColor = '#ffc61a';
        y[i].textContent = z;
    }
    else{
        y[i].style.backgroundColor = 'green';
        y[i].textContent = z;
    }
}

