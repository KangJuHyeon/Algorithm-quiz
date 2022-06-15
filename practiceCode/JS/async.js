// Async/Await
async function f1() {
    const a = await add10(10);
    const b = await add10(a);
    console.log(a, b)
  }
f1();