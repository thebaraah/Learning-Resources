package net.hackyourfuture.hyfshop.product;

import lombok.AllArgsConstructor;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.simple.JdbcClient;
import org.springframework.stereotype.Repository;
import java.util.Collection;

@Repository
@AllArgsConstructor
public class ProductRepository {
    private final JdbcClient jdbcClient;

    public static final RowMapper<Product> PRODUCT_ROW_MAPPER = (rs, _) -> Product.builder()
            .id(rs.getInt("id"))
            .title(rs.getString("title"))
            .price(rs.getBigDecimal("price"))
            .category(rs.getString("category"))
            .build();

    public Collection<Product> getAllProducts() {
        return jdbcClient
                .sql("SELECT id, title, price, category FROM products")
                .query(PRODUCT_ROW_MAPPER)
                .list();

    }
}
