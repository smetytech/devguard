<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';

	let {
		id,
		label,
		placeholder,
		value = $bindable(),
		error = $bindable()
	}: {
		id: string;
		label: string | undefined;
		placeholder: string | undefined;
		value: string | undefined;
		error: string | undefined;
	} = $props();

	function handleInput() {
		error = '';
	}
</script>

<div class="flex w-full flex-col gap-1.5">
	{#if label}
		<Label class={error && 'text-destructive'} for={id}>{label}</Label>
	{/if}

	<Input
		class="{error && 'border-destructive !ring-destructive'} truncate"
		{id}
		type="text"
		{placeholder}
		bind:value
		oninput={handleInput}
	/>

	{#if error}
		<span class="text-destructive text-[0.8rem]">{error}</span>
	{/if}
</div>
