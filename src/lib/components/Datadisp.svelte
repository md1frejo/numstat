<script>

 export let stats;
 export let classn = ""
 
 let openItems = {};
 
 function toggleValue(country,key) {
   if (!openItems[country]) {
     openItems[country] = new Set();
   }
   if (openItems[country].has(key)) {
     openItems[country].delete(key); // close it
   }
   else {
     openItems[country].add(key); // open it
   }
   openItems = { ...openItems };
 }
 
</script>

<main class={`bg-AntiqueWhiteg-200 ${classn}`}>
  <p class="text-8xl text-center text-brown4g-300">datadisp</p>
  
  {#each Object.entries(stats) as [country,details]}
    <p class="text-cent1 text-blueg-400">Country: {country}</p>
    <ul>
      {#each Object.entries(details) as [key,value]}
	{#if key === "Location"}
	  <li><strong>{key}:</strong> {value}</li>
	{:else}
	  <li>
            <button on:click={() => toggleValue(country,key)}>
              {key}
            </button>
            {#if openItems[country] && openItems[country].has(key)}
              <p class="text-brown4g-300">{value}</p>
            {/if}
	  </li>
	{/if}
      {/each}
    </ul>
  {/each}
  <p class="text-8xl max-w-cw2 bg-green4g-500 text-brown4g-300">datadisp</p>
</main>

<style>
</style>


