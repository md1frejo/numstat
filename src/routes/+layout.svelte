<script>

 import "../app.css";
 import Topbar from "$lib/components/Topbar.svelte"
 import Main from "$lib/components/Main.svelte"
 import Bottom from "$lib/components/Bottom.svelte"
 
</script>

<Topbar />
<Main />
<slot />
<Bottom />
