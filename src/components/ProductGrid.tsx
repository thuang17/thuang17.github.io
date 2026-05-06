import ProductCard from './ProductCard';

interface Product {
  title: string;
  description: string;
  tags: string[];
  status: 'building' | 'live' | 'archived';
  slug: string;
}

interface ProductGridProps {
  products: Product[];
}

export default function ProductGrid({ products }: ProductGridProps) {
  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
      gap: '16px',
    }}>
      {products.map(product => (
        <ProductCard key={product.slug} {...product} />
      ))}
    </div>
  );
}
