export interface IPricingPack {
	name: string;
	description: string;
	monthlyPrice: number;
	yearlyPrice: number;
	features: Array<string>;
	savings: string;
}
