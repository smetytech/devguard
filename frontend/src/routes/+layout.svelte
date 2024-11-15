<script lang="ts">
	import { ModeWatcher } from 'mode-watcher';
	import { Toaster } from '$lib/components/ui/sonner';
	import { UserMenu } from '$lib/components/other/user-menu';
	import 'src/app.css';

	let { children, data } = $props();
	let user = $derived(data.user);
</script>

<ModeWatcher />
<Toaster closeButton richColors />

<div>
	<div class="flex items-center justify-between p-4 lg:px-6">
		<div>
			<!--  -->
		</div>

		{#if user}
			<UserMenu {user} />
		{/if}
	</div>

	{@render children()}
</div>
