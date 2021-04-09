let x = document.querySelectorAll('.myChart');
let y= document.querySelectorAll('.myChart .showValue')

for( let i=0; i< x.length; i++){
    y[i].textContent = x[i].getAttribute('data-percent')*100 +'%'
}