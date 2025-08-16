<script>

 export let stats;
 
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

<style>
</style>

<main class="container max-w-cw1 mx-auto bg-blueg-1000">
  <p class="text-8xl text-center text-brown4g-300">center</p>
  
{#each Object.entries(stats) as [country, details]}
  <p class="text-cent1 text-blueg-400">Country: {country}</p>
  <ul>
    {#each Object.entries(details) as [key, value]}
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

</main>
