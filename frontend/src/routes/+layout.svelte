<script lang="ts">
	import { page } from '$app/stores';
	import { mode, ModeWatcher } from 'mode-watcher';
	import { Toaster } from '$lib/components/ui/sonner';
	import { UserMenu } from '$lib/components/other/user-menu';
	import 'src/app.css';

	let { children, data } = $props();

	let isAuthRoute = $derived($page.route.id?.includes('/auth'));
	let user = $derived(data.user);
</script>

<ModeWatcher />
<Toaster closeButton richColors />

<div>
	{#if !isAuthRoute}
		<header class="flex items-center justify-between p-4 lg:px-6">
			<a href="/">
				<img
					class="h-10 w-10"
					src="/assets/icons/devguard{$mode && $mode === 'dark' ? '-dark' : ''}.svg"
					alt="DevGuard"
				/>
			</a>

			<span class="block font-medium">DevGuard Agent</span>

			{#if user}
				<UserMenu {user} />
			{/if}
		</header>
	{/if}

	{@render children()}
</div>
