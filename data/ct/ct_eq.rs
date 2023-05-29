#[inline]
fn ct_eq(&self, _rhs: &[T]) -> Choice {
    let len = self.len();

    // Short-circuit on the *lengths* of the slices, not their
    // contents.
    if len != _rhs.len() {
        return Choice::from(0);
    }

    // This loop shouldn't be shortcircuitable, since the compiler
    // shouldn't be able to reason about the value of the `u8`
    // unwrapped from the `ct_eq` result.
    let mut x = 1u8;
    for (ai, bi) in self.iter().zip(_rhs.iter()) {
        x &= ai.ct_eq(bi).unwrap_u8();
    }

    x.into()
}
