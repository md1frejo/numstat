<script>

 export let stats
 export let classn=""
 export let bgleft=""

 let res1=null
 let res2=null
 let res3=null
 
 function randf() {
   
   const cts=Object.entries(stats).flatMap(([k1,v1]) => Object.entries(v1))
     const st1=Object.entries(stats).flatMap(([k1,v1]) => Object.entries(v1).map(([k2,v2]) => [k1,k2,v2]))

     let ri = Math.floor(Math.random() * st1.length);
   
   res1=st1[ri]
   res1=res1.split(' ')
   
 }

 function combf() {

   let deb=Object.entries(stats)
   
   let ke=new Set (deb.flatMap(([k,v]) => Object.entries(v)).filter(([k2,v2]) => v2.match(/\d+./)).map(([k3,v3]) => k3))
   let k1=deb.flatMap(([k,v]) => Object.entries(v).map(([k2,v2]) => [k,k2,v2])).filter(([k,k2,v2]) => v2.match(/\d+./)).map(([k,k3,v3]) => ({"country":k,"k3":k3,"v3":v3}))

   const cts=Object.entries(stats).map(x => x[1])
   const st2=Object.entries(stats).flatMap(([k1,v1]) => Object.entries(v1).map(([k2,v2]) => [k1,k2,v2]))

   let ri2=Math.floor(Math.random()*st2.length);
   let ri3=Math.floor(Math.random()*st2.length);

//   let c=k1[ri2].country
//   let k3=k1[ri2].k3

   console.log(k1)
   
   for (let k=0; k<1000; k++) {
     let i=Math.floor(Math.random()*k1.length)
     let ri2=Math.floor(Math.random()*k1.length)
     if (k1[ri2].country && k1[ri2].k3 && k1[i].country !== k1[ri2].country && k1[i].k3 === k1[ri2].k3) {
       res3=k1[i]
       res2=k1[ri2]
       break
     }
   }
   
//   res2=k1[ri2]
 }
 
</script>

<style>
</style>

<main class={`px-4 text-center ${bgleft} ${classn}`}>
  <section class="p-4 bg-lightblueg-700 mx-auto w-2/3 min-h-32">
    <button class="text-blue-600" on:click={() => randf()}>
      <p class="text-le1 text-brown4g-300">random fact1</p>
    </button>

    {#if res1!==null}
      <p class="mt-4 text-le2 text-browngrad-200">{res1[0]}:</p>
      <p class="mt-4 text-le3 text-browngrad-400">{res1[1]}:</p>
      <p class="mt-4 text-blueg-200">{res1.slice(2)}</p>
    {/if}

    <button class="text-blue-600" on:click={() => combf()}>
      <p class="text-le1 text-brown4g-300">random fact2</p>
    </button>

    {#if res2!==null && res3!==null}
      <p class="mt-4 text-browngrad-200"> {res2.country} and {res3.country} </p>
      <p class="mt-4 text-browngrad-500"> {res2.k3}  </p>
      <p class="mt-4 text-blueg-200"> {res2.v3} </p>
      <p class="mt-4 text-blueg-200"> {res3.v3} </p>
    {/if}
    
  </section>

</main>
