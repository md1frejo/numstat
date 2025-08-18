<script>

 import "../app.css";
 import Topbar from "$lib/components/Topbar.svelte"
 import Bottom from "$lib/components/Bottom.svelte"
 
</script>

<Topbar />
<slot />
<Bottom />
