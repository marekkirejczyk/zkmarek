pub struct FieldElement10x26(pub(crate) [u32; 10]);

impl FieldElement10x26 {
    pub const fn add(&self, rhs: &Self) -> Self {
        Self([
            self.0[0] + rhs.0[0],
            self.0[1] + rhs.0[1],
            self.0[2] + rhs.0[2],
            self.0[3] + rhs.0[3],
            self.0[4] + rhs.0[4],
            self.0[5] + rhs.0[5],
            self.0[6] + rhs.0[6],
            self.0[7] + rhs.0[7],
            self.0[8] + rhs.0[8],
            self.0[9] + rhs.0[9],
        ])
    }

    pub fn normalize(&self) -> Self {
        let res = self.normalize_weak();
        let overflow = res.get_overflow();
        let res_corrected = res.add_modulus_correction(1u32);
        let (res_corrected, x) = res_corrected.subtract_modulus_approximation();
        debug_assert!(x == (overflow.unwrap_u8() as u32));
        Self::conditional_select(&res, &res_corrected, overflow)
    }
}
