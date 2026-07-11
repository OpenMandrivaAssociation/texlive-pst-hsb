%global tl_name pst-hsb
%global tl_revision 66739

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Curves with continuous colours
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-hsb
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-hsb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-hsb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a PSTricks-related package. It can plot lines and/or curves with
continuous colours. Only colours defined in the hsb model are supported.

