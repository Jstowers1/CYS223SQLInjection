
export default function LIForm(){
  const sayHello = async () => {
    try{
      const res = await fetch("http://localhost:5000/hello");
      const data = await res.json();
      console.log(data);
    } catch (err) {
      console.error(err);
    }
  }

  return(
    <div>
      <p>Maybe this time it'll work...?</p>
      <form>
        <label for = "username">Enter username here pls :3</label> <br />
        <input type="text" />
        <button onClick = {sayHello} type="submit">Submit here brochado</button> <br />
      </form>
    </div>
  )
}
