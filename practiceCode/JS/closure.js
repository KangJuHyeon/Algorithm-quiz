// 클로저(Closure) 예제
function init() {
    var name = "Mozilla"; // name is a local variable created by init
    function displayName() { // displayName() is the inner function, a closure
        name = 'helloword' // displayName()도 함수이기 때문에 외부함수에 name 값을 변형시킬 수 있다.
        alert (name); // displayName() uses variable declared in the parent function    
    }
    displayName();    
}
init();