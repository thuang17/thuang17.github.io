interface ProductCardProps {
  title: string;
  description: string;
  tags: string[];
  status: 'building' | 'live' | 'archived';
  slug: string;
}

export default function ProductCard({ title, description, tags, status, slug }: ProductCardProps) {
  const statusLabels: Record<string, string> = {
    building: 'Building',
    live: 'Live',
    archived: 'Archived',
  };

  return (
    <a
      href={`/products/${slug}`}
      className="product-card"
      style={{
        display: 'block',
        padding: '24px',
        borderRadius: '12px',
        border: '1px solid var(--border)',
        background: 'var(--bg-sub)',
        textDecoration: 'none',
        color: 'inherit',
        transition: 'transform 0.2s ease, box-shadow 0.2s ease',
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = 'translateY(-2px)';
        e.currentTarget.style.boxShadow = '0 8px 24px rgba(28,25,23,0.10)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = '';
        e.currentTarget.style.boxShadow = '';
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
        <h3 style={{ fontFamily: 'var(--f-display)', fontSize: '18px', fontWeight: 700, margin: 0 }}>
          {title}
        </h3>
        <span style={{
          fontFamily: 'var(--f-mono)',
          fontSize: '11px',
          padding: '2px 8px',
          borderRadius: '999px',
          background: status === 'building' ? 'rgba(124,58,237,0.07)' : status === 'live' ? 'rgba(34,197,94,0.1)' : 'rgba(168,162,158,0.15)',
          color: status === 'building' ? 'var(--accent)' : status === 'live' ? '#16a34a' : 'var(--fg-3)',
          border: '1px solid',
          borderColor: status === 'building' ? 'rgba(124,58,237,0.20)' : status === 'live' ? 'rgba(34,197,94,0.2)' : 'rgba(168,162,158,0.2)',
          whiteSpace: 'nowrap',
        }}>
          {statusLabels[status]}
        </span>
      </div>
      <p style={{ color: 'var(--fg-2)', fontSize: '14px', lineHeight: 1.6, margin: 0 }}>
        {description}
      </p>
      {tags.length > 0 && (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px', marginTop: '12px' }}>
          {tags.map(tag => (
            <span key={tag} style={{
              fontFamily: 'var(--f-mono)',
              fontSize: '11px',
              color: 'var(--fg-3)',
              padding: '2px 8px',
              borderRadius: '4px',
              background: 'color-mix(in srgb, var(--bg) 88%, transparent)',
            }}>
              {tag}
            </span>
          ))}
        </div>
      )}
    </a>
  );
}
