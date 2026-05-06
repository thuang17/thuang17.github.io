import { defineCollection, z } from 'astro:content';

const productsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    tags: z.array(z.string()).default([]),
    status: z.enum(['building', 'live', 'archived']).default('building'),
    image: z.string().optional(),
  }),
});

export const collections = {
  products: productsCollection,
};
