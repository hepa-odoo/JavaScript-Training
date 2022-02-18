
console.log('date script initialized..');
const dateConverter = (timee) => {
    let millsec = timee%1000;
    timee /= 1000;
    let sec = Math.floor(timee)%60;
    timee /= 60;
    let mini = Math.floor(timee)%60;
    timee /= 60;
    let hour = Math.floor(timee)%24;
    timee /= 24;
    let day = Math.floor(timee)%30;
    return `${day} ${hour}:${mini}:${sec}:${millsec}`;
}

console.log(dateConverter(8000000));