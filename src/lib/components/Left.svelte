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

   const cts=Object.entries(stats).map(x => x[1])
   let deb=Object.entries(stats)
   console.log(deb)
   const st2=Object.entries(stats).flatMap(([k1,v1]) => Object.entries(v1).map(([k2,v2]) => [k1,k2,v2]))

     let ri2 = Math.floor(Math.random() * st2.length);
   let ri3 = Math.floor(Math.random() * st2.length);
   
   res2=st2[ri2]
   res3=st2[ri3]
   
 }
 
</script>

<style>
</style>

<main class={`px-4 text-center ${bgleft} ${classn}`}>
  <section class="p-4 bg-lightblueg-700 mx-auto w-2/3 min-h-32">
    <p class="text-ca1">random</p>
    <button class="underline text-blue-600" on:click={() => randf()}>
      <p class="text-le1 text-brown4g-300">random fact</p>
    </button>

    {#if res1!==null}
      <p class="mt-4 text-le2 text-browngrad-200">{res1[0]}:</p>
      <p class="mt-4 text-le3 text-browngrad-400">{res1[1]}:</p>
      <p class="mt-4 text-blueg-200">{res1.slice(2)}</p>
    {/if}

    <button class="underline text-blue-600" on:click={() => combf()}>
      <p class="text-le1 text-brown4g-300">debug</p>
    </button>

    {#if res2!==null && res3!==null}
      <p class="mt-4 text-browngrad-200">{res2[0]} and {res3[0]}</p>
      <p class="mt-4 text-browngrad-200">{res2[1]}</p>
      <p class="mt-4 text-browngrad-200">{res2[2]}</p>
    {/if}
    
  </section>

</main>
