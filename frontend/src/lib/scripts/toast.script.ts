import { toast } from 'svelte-sonner';

export function displayGeneralErrorToast() {
	toast.error('An unexpected error occurred. Please try again later.');
}
