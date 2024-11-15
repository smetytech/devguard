<script lang="ts">
	import { ModeWatcher } from 'mode-watcher';
	import { Toaster } from '$lib/components/ui/sonner';
	import 'src/app.css';

	let { children } = $props();
</script>

<ModeWatcher />
<Toaster closeButton richColors />

{@render children()}
