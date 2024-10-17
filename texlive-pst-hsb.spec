Name:		texlive-pst-hsb
Version:	66739
Release:	1
Summary:	Curves with continuous colours
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-hsb
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-hsb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-hsb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks-related package. It can plot lines and/or
curves with continuous colours. Only colours defined in the hsb
model are supported

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-hsb
%{_texmfdistdir}/tex/generic/pst-hsb
%doc %{_texmfdistdir}/doc/generic/pst-hsb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
