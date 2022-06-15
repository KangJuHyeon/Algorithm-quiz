// Promise
function add10(a) {
    return new Promise(resolve => setTimeout(() => resolve(a + 10), 100));
  } //Promise사용 시 작업이 끝났음을 알려주는 resolve를 인자로 받아들임.
  add10(10)
    .then(add10)
    .then(add10)
    .then(add10)
    .then((res) => console.log(res))

// Promise에서의 예외 처리
add10(10)
  .then((res) => {
        throw 'test error';
    })
  .catch((err) => console.log(err));

// 비동기 함수
async function main() {
    console.log("1");
    
    setTimeout(()=>{
        console.log("2");
    }, 1000);
    
    console.log("3");
    
    await new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("4");
            resolve();
        }, 1000);
    });

    console.log("5");
}
main();
