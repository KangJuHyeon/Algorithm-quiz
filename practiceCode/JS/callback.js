// 콜백 함수
function Callback(callback){
    console.log('콜백 함수');
    callback();
}
Callback(function(){
    console.log('콜백 받는곳');
})

// 무한 콜백함수
function Callback(callback){
    function Callback2(callback){
        function Callback3(callback){
            console.log('무한콜백');
        }
    }
}