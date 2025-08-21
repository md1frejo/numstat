<script>

 import "../app.css";
 import Topbar from "$lib/components/Topbar.svelte"
 import Bottom from "$lib/components/Bottom.svelte"

 export let data
 
</script>

<Topbar bgtop={data.bgtop} />
<slot />
<Bottom bgbottom={data.bgbottom} />l
