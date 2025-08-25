<script>
 import { MessageSquareDiff,Shuffle } from "lucide-svelte";
 
 export let stats
 export let classn=""
 export let bglefta=""
 export let bgleftb=""
 export let bgleft=""
 
 let res1=null
 let res2=null
 let res3=null
 let res4=null
 let res5=null
 let res6=null
 let res7=null
 
 function randf() {
   
   const cts=Object.entries(stats).flatMap(([k1,v1]) => Object.entries(v1))
   const st1=Object.entries(stats).flatMap(([k1,v1]) => Object.entries(v1).map(([k2,v2]) => [k1,k2,v2]))

   let ri = Math.floor(Math.random() * st1.length);
   
   res1=st1[ri]
   res1=res1.split(' ')
   
 }

 const deb=Object.entries(stats)
 
 function combf(deb) {
   
   let ke=new Set (deb.flatMap(([k,v]) => Object.entries(v)).filter(([k2,v2]) => v2.match(/\d+./)).map(([k3,v3]) => k3))
   let k1=deb.flatMap(([k,v]) => Object.entries(v).map(([k2,v2]) => [k,k2,v2])).filter(([k,k2,v2]) => v2.match(/\d+./)).map(([k,k3,v3]) => ({"country":k,"k3":k3,"v3":v3}))
   
   for (let k=0; k<1000; k++) {
     let i=Math.floor(Math.random()*k1.length)
     let ri2=Math.floor(Math.random()*k1.length)
     if (k1[ri2].country && k1[ri2].k3 && k1[i].country !== k1[ri2].country && k1[i].k3 === k1[ri2].k3) {
       res3=k1[i]
       res2=k1[ri2]
       break
     }
   }
 }

 function combf2(deb) {

   let ke=new Set (deb.flatMap(([k,v]) => Object.entries(v)).filter(([k2,v2]) => v2.match(/\d+./)).map(([k3,v3]) => k3))
   let k1=deb.flatMap(([k,v]) => Object.entries(v).map(([k2,v2]) => [k,k2,v2])).filter(([k,k2,v2]) => v2.match(/\d+./)).map(([k,k3,v3]) => ({"country":k,"k3":k3,"v3":v3}))
   //   console.log(k1)
   for (let k=0; k<1000; k++) {
     let i=Math.floor(Math.random()*k1.length)
     let ri2=Math.floor(Math.random()*k1.length)
     if (k1[ri2].country && k1[ri2].k3 && k1[i].country !== k1[ri2].country &&
	 k1[i].k3==="Area" && k1[ri2].k3==="Area"
     ) {
       res4=k1[i]
       res5=k1[ri2]
       break
     }
   }
 }

 function combf3(deb) {

   let ke=new Set (deb.flatMap(([k,v]) => Object.entries(v)).filter(([k2,v2]) => v2.match(/\d+./)).map(([k3,v3]) => k3))
   let k1=deb.flatMap(([k,v]) => Object.entries(v).map(([k2,v2]) => [k,k2,v2])).filter(([k,k2,v2]) => v2.match(/\d+./)).map(([k,k3,v3]) => ({"country":k,"k3":k3,"v3":v3}))
   console.log(k1)
   for (let k=0; k<1000; k++) {
     let i=Math.floor(Math.random()*k1.length)
     let ri2=Math.floor(Math.random()*k1.length)
     if (k1[ri2].country && k1[ri2].k3 && k1[i].country !== k1[ri2].country &&
	 k1[i].k3==="GDP per capita" && k1[ri2].k3==="GDP per capita"
     ) {
       res6=k1[i]
       res7=k1[ri2]
       break
     }
   }
 }
 
</script>

<style>
</style>

<main class={`px-4 text-center ${bgleft} ${classn}`}>
  <section class={`p-4 ${bgleft} mx-auto w-4/3 min-h-32`}>
    <div class="flex items-center justify-center space-x-4">
      <Shuffle class="w-7 h-7 text-blueg-600"/>
      <p class="text-le4 text-blueg-200">random facts</p>
    </div>
    <br>

    <button class="text-le1 text-brown4g-300 text-blue-600" on:click={() => randf()}>
      random fact
    </button>

    {#if res1!==null}
      <p class="mt-4 text-le2 text-browngrad-200">{res1[0]}:</p>
      <p class="mt-4 text-le3 text-browngrad-400">{res1[1]}:</p>
      <p class="mt-4 text-blueg-200">{res1.slice(2)}</p>
    {/if}
    <br>
    <br>
    <button class="text-blue-600" on:click={() => combf(deb)}>
      <span class="text-le1 text-brown4g-300">more random</span>
    </button>

    {#if res2!==null && res3!==null}
      <p class="mt-4 text-browngrad-200"> {res2.country} and {res3.country} </p>
      <p class="mt-4 text-browngrad-500"> {res2.k3}  </p>
      <p class="mt-4 text-blueg-200"> {res2.v3} </p>
      <p class="mt-4 text-blueg-200"> {res3.v3} </p>
    {/if}
    <br>
    <br>
    <button class="text-blue-600" on:click={() => combf2(deb)}>
      <span class="text-le1 text-brown4g-300">Area</span>
    </button>

    {#if res4!==null && res5!==null}
      <p class="mt-4 text-browngrad-200"> {res4.country} and {res5.country} </p>
      <p class="mt-4 text-browngrad-500"> {res4.k3}  </p>
      <p class="mt-4 text-blueg-200">  {res4.country}: {res4.v3} </p>
      <p class="mt-4 text-blueg-200"> {res5.country}: {res5.v3} </p>
    {/if}
    <br>
    <br>
    <button class="text-blue-600" on:click={() => combf3(deb)}>
      <span class="text-le1 text-brown4g-300">GDP</span>
    </button>

    {#if res6!==null && res7!==null}
      <p class="mt-4 text-browngrad-200"> {res6.country} and {res7.country} </p>
      <p class="mt-4 text-browngrad-500"> {res6.k3}  </p>
      <p class="mt-4 text-blueg-200"> {res6.country}: {res6.v3} </p>
      <p class="mt-4 text-blueg-200"> {res7.country}: {res7.v3} </p>
    {/if}
    
  </section>

</main>
