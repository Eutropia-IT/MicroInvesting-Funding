let x = document.querySelectorAll('.indecator input');
let y = document.querySelectorAll('.indecator label');
console.log(x)

for(let i=0; i<x.length; i++){
    
    if(x[i].value < 5){
        y[i].style.backgroundColor = '#ff4c4c';
        y[i].textContent = x[i].value;
    }
    else if(x[i].value >= 5 && x[i].value< 8){
        y[i].style.backgroundColor = '#ffc61a';
        y[i].textContent = x[i].value;
    }
    else{
        y[i].style.backgroundColor = 'green';
        y[i].textContent = x[i].value;
    }
}